import os
import json
import sys

import requests
import webbrowser
import subprocess

from PySide6.QtWidgets import QMessageBox, QPushButton, QDialogButtonBox, QMainWindow

import RLDebug
import global_var

from ui_form_update import Ui_FormUpdate

global rlUpdate


class RLUpdate(QMainWindow):

    def __init__(self):

        # 加载更新弹窗UI
        super(RLUpdate, self).__init__()
        self.ui = Ui_FormUpdate()
        self.ui.setupUi(self)

        # 设置窗口图标
        self.setWindowIcon(global_var.app_icon())

        # 最新版本信息
        self.json_data = {}

        # 弹窗按钮
        button_web = QPushButton('打开发布页面')
        button_download = QPushButton('下载更新')
        button_cancel = QPushButton('取消')
        button_ignore = QPushButton('此版本不再提醒')

        # 将按钮添加到弹窗
        self.ui.buttonBox.addButton(button_download, QDialogButtonBox.ButtonRole.AcceptRole)
        self.ui.buttonBox.addButton(button_web, QDialogButtonBox.ButtonRole.AcceptRole)
        self.ui.buttonBox.addButton(button_cancel, QDialogButtonBox.ButtonRole.RejectRole)
        self.ui.buttonBox.addButton(button_ignore, QDialogButtonBox.ButtonRole.RejectRole)

        # 绑定按钮事件
        button_web.clicked.connect(self.open_publish_page)
        button_download.clicked.connect(self.download_update)
        button_ignore.clicked.connect(self.ignore_update)

        RLDebug.debug("更新提示模块初始化完成", type='success', who=self.__class__.__name__)

    def set_data(self, data):
        # 设置最新版本数据并显示
        self.json_data = data

        update_info = "发现新版本，是否更新？" \
                      "\n-----更新信息-----" \
                      "\n当前版本: {}" \
                      "\n最新版本: {}" \
                      "\n发布时间: {}" \
                      "\n文件大小: {} bytes ({} MB)" \
                      "\n更新说明: {}" \
            .format(global_var.current_version,
                    self.json_data['tag_name'],
                    self.json_data['published_at'],
                    self.json_data['assets'][0]['size'],
                    self.json_data['assets'][0]['size'] / 1000000,
                    self.json_data['body'])

        self.ui.textInfo.setText(update_info)

    def open_publish_page(self):

        # 打开最新版本发布页面
        RLDebug.debug("已打开最新版本发布页面", type='success', who=self.__class__.__name__)
        webbrowser.open(self.json_data['html_url'])

    def install_update(self):

        RLDebug.debug("更新文件{}已经就绪，准备进行更新".format(os.path.join(os.getcwd(), self.json_data['assets'][0]['name'])),
                      type='success',
                      who=self.__class__.__name__)
        msgbox = QMessageBox()
        msgbox.setWindowTitle("确认进行更新")
        msgbox.setText("你确定要自动安装更新吗？")
        msgbox.setInformativeText("当前版本的内容将被覆盖")
        msgbox.setIcon(QMessageBox.StandardButton.Question)
        msgbox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msgbox.setDefaultButton(QMessageBox.StandardButton.Yes)
        msgbox.setButtonText(QMessageBox.StandardButton.Yes, "确定")
        msgbox.setButtonText(QMessageBox.StandardButton.No, "手动安装更新")
        ret = msgbox.exec_()
        if ret == QMessageBox.StandardButton.Yes:
            RLDebug.debug("用户已经确认，开始生成更新脚本" + os.path.join(os.getcwd(), "update.bat"),
                          type='info',
                          who=self.__class__.__name__)
            bat = open("update.bat", 'w')
            update_script = "@echo off \n"
            update_script += "if not exist RogueLifePy.zip exit \n"
            update_script += "timeout 3 \n"
            update_script += "tar -xf RogueLifePy.zip \n"
            update_script += "del RogueLifePy.zip \n"
            update_script += "start RogueLifePy.exe"
            bat.write(update_script)
            bat.close()
            RLDebug.debug("成功生成更新脚本" + os.path.join(os.getcwd(), "update.bat"),
                          type='success',
                          who=self.__class__.__name__)
            QMessageBox.warning(self, "游戏需要重启", "游戏即将重启以更新到最新版本")
            RLDebug.debug("退出主程序并开始运行更新脚本" + os.path.join(os.getcwd(), "update.bat"),
                          type='info',
                          who=self.__class__.__name__)
            subprocess.Popen("update.bat")
            sys.exit()
        else:
            QMessageBox.information(self, "更新文件下载完成", "更新文件已保存至{}\n请手动解压并覆盖当前版本"
                                    .format(os.path.join(os.getcwd(), self.json_data['assets'][0]['name'])))

    def download_update(self):
        # 下载最新版本更新文件

        # 检测是否已经存在更新文件
        if os.path.exists(self.json_data['assets'][0]['name']):
            RLDebug.debug("发现已下载的更新文件{},跳过本次下载".format(self.json_data['assets'][0]['name']),
                          type='warn',
                          who=self.__class__.__name__)
            self.install_update()
            return

        # 下载更新文件
        RLDebug.debug("开始下载更新文件{}".format(self.json_data['assets'][0]['browser_download_url']),
                      who=self.__class__.__name__)
        try:
            update_file = requests.get(self.json_data['assets'][0]['browser_download_url'])
        except requests.exceptions.ConnectionError:
            RLDebug.debug("网络连接异常，下载更新文件失败", type='error', who=self.__class__.__name__)
            return

        RLDebug.debug("已下载更新文件" + self.json_data['assets'][0]['name'],
                      type='success',
                      who=self.__class__.__name__)
        RLDebug.debug("正在保存更新文件到" + os.path.join(os.getcwd(), self.json_data['assets'][0]['name']),
                      who=self.__class__.__name__)

        # 保存更新文件到运行目录
        with open(self.json_data['assets'][0]['name'], 'wb') as f:
            f.write(update_file.content)
            f.close()
        RLDebug.debug("更新文件已保存至" + os.path.join(os.getcwd(), self.json_data['assets'][0]['name']),
                      type='success',
                      who=self.__class__.__name__)
        self.install_update()

    def ignore_update(self):

        # 弹窗询问是否跳过当前版本更新
        msgbox = QMessageBox()
        msgbox.setWindowTitle("确认跳过版本")
        msgbox.setText("你确定要跳过当前版本更新吗？")
        msgbox.setInformativeText("你将不再收到当前版本的更新推送")
        msgbox.setIcon(QMessageBox.Icon.Question)
        msgbox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msgbox.setDefaultButton(QMessageBox.StandardButton.Yes)
        msgbox.setButtonText(QMessageBox.StandardButton.Yes, "确定")
        msgbox.setButtonText(QMessageBox.StandardButton.No, "再想想")
        ret = msgbox.exec_()
        if ret == QMessageBox.StandardButton.Yes:

            # 将当前已忽略的版本和新忽略的版本序列化
            ignored_version = [self.json_data['tag_name']]
            if 'ignored_version' in global_var.configs.config_keys():
                for ver in global_var.configs.get_config('ignored_version'):
                    ignored_version.append(ver)
            RLDebug.debug("当前跳过的版本: {}".format(ignored_version))
            json_dump = {'name': 'ignore_update',
                         'type': 'config',
                         'version': global_var.current_version,
                         'enabled': True, 
                         'ignored_version': [self.json_data['tag_name']]}

            # 保存配置文件
            with open(os.path.join(os.getcwd(), 'data', 'ignored_version.json'), "w+") as f:
                json.dump(json_dump, f)

            RLDebug.debug("配置文件已保存至" + os.path.join(os.getcwd(), 'data', 'ignored_version.json'))


def init():
    global rlUpdate
    rlUpdate = RLUpdate()


def display():
    RLDebug.debug("已打开更新提示界面", type='success', who='RLUpdate')
    rlUpdate.ui.show()


def set_data(data):
    rlUpdate.set_data(data)
