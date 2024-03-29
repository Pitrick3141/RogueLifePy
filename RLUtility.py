import hashlib
import json
import os
import platform
import subprocess

import requests
from PySide6.QtWidgets import QMessageBox, QFileDialog, QMainWindow
from threading import Thread

import RLConsole
import RLDataFiles
import RLEditor
import RLItems
import RLPlayer
import global_var
import RLDebug
import RLUpdate

from ui.ui_form_utility import Ui_FormUtility

global rlMenu


class RLMenu(QMainWindow):
    def __init__(self):
        # 加载菜单UI
        super(RLMenu, self).__init__()
        self.ui = Ui_FormUtility()
        self.ui.setupUi(self)

        # 设置窗口图标
        self.setWindowIcon(global_var.app_icon())

        # 是否是启动第一次检查更新
        self.first_check = True

        # 绑定按钮事件
        self.ui.buttonOpenDataFilesDir.clicked.connect(self.open_dir)
        self.ui.buttonImportDataFile.clicked.connect(self.import_data_files)
        self.ui.buttonSyncDataFiles.clicked.connect(self.sync_data_files)
        self.ui.buttonCheckUpdate.clicked.connect(self.check_update)
        self.ui.buttonDebug.clicked.connect(self.show_debug)
        self.ui.buttonConsole.clicked.connect(self.show_console)
        self.ui.buttonOpenEditor.clicked.connect(self.show_editor)

    def check_update(self):

        # 检查应用更新
        latest = True
        RLDebug.debug("开始检查更新", who=self.__class__.__name__)

        # 获取Github Repo信息
        try:
            r = requests.get(url='https://api.github.com/repos/Pitrick3141/RogueLifePy/releases/latest')
        except requests.exceptions.ConnectionError:
            RLDebug.debug("网络连接异常，检查更新失败", type='error', who=self.__class__.__name__)
            return

        # 反序列化json数据
        json_data = r.json()

        if 'tag_name' not in json_data:
            RLDebug.debug("网络连接异常，检查更新失败", type='error', who=self.__class__.__name__)
            return

        RLDebug.debug("检查更新完成", type='success', who=self.__class__.__name__)

        # 最新版本号
        latest_version = json_data['tag_name']

        # 拆分最新版本号和当前版本号以便比较
        cmp_version = latest_version[1:].split('.')
        cmp_current = global_var.current_version[1:].split('.')

        # 发布日期
        publish_time = json_data['published_at']
        # 发布文件
        assets = json_data['assets']
        # 发布文件大小
        file_size = assets[0]['size']
        # 文件描述
        file_des = json_data['body']

        RLDebug.debug("检查更新结果:"
                      "<br>----------"
                      "<br>当前版本: {}"
                      "<br>最新版本: {}"
                      "<br>最新版本发布时间: {}"
                      "<br>发布文件大小: {} bytes ({} MB)"
                      "<br>最新版本更新说明: {}"
                      "<br>----------"
                      .format(global_var.current_version,
                              latest_version,
                              publish_time,
                              file_size,
                              file_size / 1000000,
                              file_des), who=self.__class__.__name__)

        # 比较最新版本号和当前版本号
        for v in range(len(cmp_version)):
            if int(cmp_version[v]) > int(cmp_current[v]):
                latest = False
                break
            elif int(cmp_version[v]) < int(cmp_current[v]):
                RLDebug.debug("当前版本号较最新版本号更高，可能存在错误", type='warn', who=self.__class__.__name__)
                break
            else:
                continue

        # 若当前版本不是最新
        if not latest:

            # 检测是否忽略了新版本更新
            if 'ignored_version' in global_var.configs.config_keys():
                if latest_version in global_var.configs.get_config('ignored_version'):
                    RLDebug.debug("发现新版本{}，但已被配置项忽视，跳过本次更新".format(latest_version),
                                  type='warn',
                                  who=self.__class__.__name__)
                    return

            # 弹窗提示更新
            RLDebug.debug("发现新版本，已弹出提示窗口", type='warn', who=self.__class__.__name__)
            RLUpdate.set_data(json_data)
            RLUpdate.display()

        else:
            RLDebug.debug("当前已经是最新版本", type='success', who=self.__class__.__name__)
            if not self.first_check:
                QMessageBox.information(self, "检查更新完成", "当前已经是最新版本: " + global_var.current_version)

        self.first_check = False

    def sync_data_files(self):
        # 同步计数
        cnt_found = 0
        cnt_new = 0
        cnt_existed = 0
        cnt_changed = 0
        cnt_downloaded = 0

        # 从Github同步数据文件
        RLDebug.debug("开始同步数据文件", who=self.__class__.__name__)

        # 若不存在数据文件目录则建立数据文件目录
        if not os.path.exists("data"):
            os.mkdir("data")

        try:
            r = requests.get(url='https://api.github.com/repos/Pitrick3141/RogueLifePy/contents/data',
                             params={'ref': 'master'})
        except requests.exceptions.ConnectionError:
            RLDebug.debug("网络连接异常，同步数据文件失败", type='error', who=self.__class__.__name__)
            return

        # 反序列化json数据
        json_data = r.json()

        RLDebug.debug("已获取数据文件列表", type='success', who=self.__class__.__name__)

        # 新数据文件列表
        new_data_files = []

        # 遍历云端数据文件列表
        for data_file in json_data:

            # 大小为0则跳过
            if data_file['size'] == 0:
                continue

            cnt_found += 1

            # 获取数据文件信息
            name = data_file['name'].replace('.json', '')
            name = name.lower()
            sha = data_file['sha']
            file_size = data_file['size']
            download_url = data_file['download_url']

            # 检查是否有新数据文件
            if name not in global_var.data_files_hash.values():
                cnt_new += 1

                RLDebug.debug("发现新数据文件: {}<br>大小: {} Bytes".format(name, file_size), who=self.__class__.__name__)

                # 加入新数据文件列表中
                new_data_files.append((name, file_size, download_url))

            # 重名数据文件检查哈希值是否相同
            elif sha not in global_var.data_files_hash.keys():
                cnt_changed += 1

                # 哈希值不同弹窗确认是否覆盖
                RLDebug.debug("发现改动的数据文件: {}<br>大小: {} Bytes,<br>hash: {}, 已弹窗询问".format(name, file_size, sha),
                              who=self.__class__.__name__)
                msgbox = QMessageBox()
                msgbox.setWindowTitle("下载数据文件确认")
                msgbox.setText("云端数据文件与本地数据文件同名但内容不同\n是否覆盖下载？")
                msgbox.setInformativeText("当前本地同名数据文件:{}".format(os.path.join(os.getcwd(), 'data', name + '.json')))
                msgbox.setIcon(QMessageBox.Icon.Warning)
                msgbox.setStandardButtons(QMessageBox.StandardButton.Yes |
                                          QMessageBox.StandardButton.Ok |
                                          QMessageBox.StandardButton.No)
                msgbox.setDefaultButton(QMessageBox.StandardButton.Yes)
                msgbox.setButtonText(QMessageBox.StandardButton.Yes, "覆盖下载")
                msgbox.setButtonText(QMessageBox.StandardButton.Ok, "重命名下载")
                msgbox.setButtonText(QMessageBox.StandardButton.No, "不下载")
                ret = msgbox.exec_()

                if ret == QMessageBox.StandardButton.Yes:
                    # 覆盖下载
                    RLDebug.debug("已选择覆盖下载数据文件: {}".format(name), who=self.__class__.__name__)
                    if self.download_data_files(download_url, name):
                        cnt_downloaded += 1

                elif ret == QMessageBox.StandardButton.Ok:
                    # 重命名下载
                    RLDebug.debug("已选择重命名下载数据文件: {}".format(name), who=self.__class__.__name__)
                    if self.download_data_files(download_url, name + "_云端同步"):
                        cnt_downloaded += 1
                else:
                    # 不下载
                    RLDebug.debug("已选择不下载数据文件: {}, 跳过同步".format(name), type='warn', who=self.__class__.__name__)

            else:
                cnt_existed += 1
                RLDebug.debug("数据文件已存在: {}, 跳过同步".format(global_var.data_files_hash.get(sha)),
                              type='warn',
                              who=self.__class__.__name__)

        # 弹窗提示并下载所有新数据文件
        if len(new_data_files) > 0:
            str_new_data_files = "是否下载如下{}个新数据文件:\n".format(len(new_data_files))
            for (temp_name, temp_size, temp_url) in new_data_files:
                str_new_data_files += "数据名称: {}.json 数据大小: {}Bytes ({}MB)\n".format(
                    temp_name,
                    temp_size,
                    temp_size / 1000000)
            ret = QMessageBox.question(self, "下载数据确认", str_new_data_files)

            if ret == QMessageBox.StandardButton.Yes:
                for (temp_name, temp_size, temp_url) in new_data_files:
                    if self.download_data_files(temp_url, temp_name):
                        cnt_downloaded += 1

        # 刷新数据文件列表
        if not cnt_downloaded == 0:
            RLDataFiles.load_data_files()

        sync_report = "数据文件同步完成" \
                      "\n在云端共发现了{}个数据文件".format(cnt_found)

        if cnt_found == cnt_existed:
            sync_report += "\n所有数据文件已是最新！"
        else:
            sync_report += "\n其中{}个数据文件已是最新".format(cnt_existed)

        if cnt_changed != 0:
            sync_report += "\n{}个数据文件有变动".format(cnt_changed)

        if cnt_new != 0:
            sync_report += "\n{}个数据文件在本地不存在".format(cnt_new)

        if cnt_downloaded != 0:
            sync_report += "\n本次同步共下载了{}个数据文件".format(cnt_downloaded)

        RLDebug.debug(sync_report,
                      type='success',
                      who=self.__class__.__name__)

        QMessageBox.information(self, "数据文件同步完成", sync_report)

    @staticmethod
    def download_data_files(url, name) -> bool:
        RLDebug.debug("开始从{}下载数据文件".format(url), who='RLMenu')
        try:
            r = requests.get(url=url)
        except requests.exceptions.ConnectionError:
            RLDebug.debug("网络连接异常，数据文件下载失败", type='error', who='RLMenu')
            return False

        content = r.json()
        with open(os.path.join('data', name + '.json'), "w") as f:
            json.dump(content, f)
        RLDebug.debug("数据文件已保存至{}".format(os.path.join(os.getcwd(), 'data', name + '.json')),
                      type='success',
                      who='RLMenu')

        return True

    def import_data_files(self):

        # 打开选择文件对话框
        file_dialog = QFileDialog(self)
        file_dir = file_dialog.getOpenFileName(self, "导入数据文件", os.getcwd(), "数据文件 (*.json)")

        # 若未选择任何文件就关闭对话框
        if file_dir[0] == "":
            RLDebug.debug("已取消导入数据文件", type='warn', who=self.__class__.__name__)
            return

        # 打开选择的文件并导入
        RLDebug.debug("正在尝试导入数据文件{0}...".format(file_dir[0]), who=self.__class__.__name__)

        with open(file_dir[0], 'rb') as f:
            # hash
            data = f.read()
            hash_obj = hashlib.sha1()
            hash_str = "blob %u\0" % len(data) + data.decode('utf-8')
            hash_obj.update(hash_str.encode('utf-8'))
            hash_value = hash_obj.hexdigest()

        with open(file_dir[0], 'rb') as load_json:

            # 数据文件字典
            data = {}
            # 缺少的键值对
            missed_keys = []
            # 显示的相对路径名称
            display_name = file_dir[0]

            # 尝试读取数据文件并转换为字典
            try:
                original_data = json.load(load_json)

            # 解码失败异常：一般是内容为空或者不合法
            except json.decoder.JSONDecodeError:
                RLDebug.debug("已损坏的数据文件：{0}, 数据文件内容为空或不合法, 跳过当前数据文件".format(display_name),
                              type='error',
                              who=self.__class__.__name__)
                return
            except UnicodeDecodeError:
                RLDebug.debug("已损坏的数据文件：{0}, 数据文件编码格式有误, 跳过当前数据文件".format(display_name),
                              type='error',
                              who=self.__class__.__name__)
                return

            # 将键全部转换为小写，避免大小写混淆
            for key, value in original_data.items():
                data[key.lower()] = value

            # 检测是否是配置文件
            if 'config' in data.keys():
                RLDebug.debug("发现配置文件：{0}, 开始解析".format(display_name), who=self.__class__.__name__)
                # RLMain.applyConfig(data)
                return

            # 检测是否有缺失的必需键值对
            for checked_key in ['name', 'type', 'version']:
                if checked_key not in data.keys():
                    missed_keys.append(checked_key)

            # 如果有缺失的关键键值对
            if not len(missed_keys) == 0:
                RLDebug.debug("已损坏的数据文件：{0}, 缺失如下键值对:{1}, 跳过当前数据文件"
                              .format(display_name, missed_keys),
                              type='error',
                              who=self.__class__.__name__)
                return

            # 检测是否已经添加了相同的数据文件
            elif hash_value in global_var.data_files_hash.keys():
                RLDebug.debug("已经载入相同的数据文件: {0}, 跳过当前数据文件"
                              .format(global_var.data_files_hash.get(hash_value)),
                              type='warn',
                              who=self.__class__.__name__)
                return

            global_var.data_files_hash[hash_value] = data.get('name')
            global_var.data_files.append(data)
            # 将数据文件添加到数据文件列表中

            # 检测是否是配置文件
            if data.get('type') == 'config':
                RLDebug.debug("发现配置文件：{0}, 开始解析".format(display_name),
                              who='DataFiles')
                global_var.configs.apply_config(data)

            # 检测是否是物品数据文件
            if data.get('type') == 'item':
                RLDebug.debug("发现物品数据文件：{0}, 开始解析".format(display_name),
                              who='DataFiles')
                RLItems.load_items(data)

            # 检测是否是玩家信息存档文件
            if data.get('type') == 'player':
                RLDebug.debug("发现玩家信息存档文件：{0}, 开始解析".format(display_name),
                              who='DataFiles')
                RLPlayer.load_player_info(data)

        RLDebug.debug("已载入数据文件: " + data.get('name'), type='success', who=self.__class__.__name__)

    @staticmethod
    def show_debug():
        # 显示调试输出
        RLDebug.display()

    @staticmethod
    def show_console():
        # 显示控制台
        RLConsole.display()

    @staticmethod
    def show_editor():
        # 显示编辑器
        RLEditor.display()

    @staticmethod
    def open_dir():
        # 打开数据文件目录
        RLDebug.debug("已打开数据文件目录", type='success', who='RLMenu')
        file_dir = os.path.join(os.getcwd(), 'data')
        if 'mac' in platform.platform().lower():
            subprocess.call(["open", file_dir])
        else:
            os.startfile(file_dir)


def init():
    global rlMenu
    rlMenu = RLMenu()


def display():
    rlMenu.show()
    RLDebug.debug("已打开功能菜单界面", type='success', who='RLMenu')


def set_debug_button_visible(is_visible):
    if is_visible:
        rlMenu.ui.buttonDebug.setVisible(True)
    else:
        rlMenu.ui.buttonDebug.setVisible(False)
    return


def set_console_button_visible(is_visible):
    if is_visible:
        rlMenu.ui.buttonConsole.setVisible(True)
    else:
        rlMenu.ui.buttonConsole.setVisible(False)
    return


def set_editor_button_visible(is_visible):
    if is_visible:
        rlMenu.ui.buttonOpenEditor.setVisible(True)
    else:
        rlMenu.ui.buttonOpenEditor.setVisible(False)
    return


def sync_data_files():
    rlMenu.sync_data_files()
    return


def check_update():
    thread_check_update = Thread(target=rlMenu.check_update)
    thread_check_update.start()
    return
