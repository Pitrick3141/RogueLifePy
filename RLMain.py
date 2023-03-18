import json
import os
import sys
import time

from PySide6.QtWidgets import QMainWindow, QMessageBox

import RLGame
import RLDebug
import RLUtility
import global_var

from ui.ui_form_main import Ui_FormMain

global rlMain


class RLMain(QMainWindow):

    def __init__(self):
        # 加载主窗口UI
        super(RLMain, self).__init__()
        self.ui = Ui_FormMain()
        self.ui.setupUi(self)

        # 设置窗口图标
        self.setWindowIcon(global_var.app_icon())

        # 彩蛋按钮
        self.refresh_egg()

        # 绑定按钮事件
        self.ui.buttonQuit.clicked.connect(quit_program)
        self.ui.buttonEggs.clicked.connect(self.show_eggs)
        self.ui.buttonMenu.clicked.connect(open_menu)
        self.ui.buttonStart.clicked.connect(self.start_game)
        self.ui.buttonAbout.clicked.connect(self.show_about)
        self.ui.buttonRecord.clicked.connect(self.show_record)

        # 清理更新脚本
        if os.path.isfile("update.bat"):
            RLDebug.debug("发现更新脚本，已清理完成", type='success', who=self.__class__.__name__)
            os.remove("update.bat")
            QMessageBox.information(self, "更新完成", "已成功更新至{}".format(global_var.current_version))

        RLDebug.debug("主界面初始化完成", type='success', who=self.__class__.__name__)

        self.about_cnt = 0
        self.record_cnt = 0

    def show_eggs(self):
        discovered_eggs = global_var.configs.get_config('discovered_eggs')
        eggs_list = ""
        for key in discovered_eggs.keys():
            eggs_list += "【{}】 发现时间: {}\n".format(key, discovered_eggs[key])
        QMessageBox.information(self, "恭喜你已经找到了{}个彩蛋".format(len(discovered_eggs)), eggs_list)

    def find_egg(self, title):
        if 'discovered_eggs' not in global_var.configs.config_keys():
            global_var.configs.set_config('discovered_eggs', {})
        discovered_eggs = global_var.configs.get_config('discovered_eggs')
        if title not in discovered_eggs.keys():
            discovered_eggs[title] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            global_var.configs.set_config('discovered_eggs', discovered_eggs)
        RLDebug.debug("发现了彩蛋【{}】, 总计已发现彩蛋{}个".format(title, len(discovered_eggs)),
                      who=self.__class__.__name__)
        json_dump = {'name': 'discovered_eggs', 'type': 'config', 'enabled': True, 'version': '*',
                     'discovered_eggs': discovered_eggs}

        # 保存配置文件
        with open(os.path.join('data', 'discovered_eggs.json'), "w") as f:
            json.dump(json_dump, f)
        RLDebug.debug("配置文件已保存至{}".format(os.path.join(os.getcwd(), 'data', 'discovered_eggs.json')),
                      who=self.__class__.__name__)

        # 刷新彩蛋按钮
        self.refresh_egg()

    def start_game(self):

        # 打开游戏界面并且隐藏当前界面
        RLGame.display()
        self.hide()

    def refresh_egg(self):
        discovered_eggs = global_var.configs.get_config('discovered_eggs')
        if not discovered_eggs:
            self.ui.buttonEggs.setVisible(False)
            return
        if len(discovered_eggs) > 0:
            self.ui.buttonEggs.setVisible(True)
            self.ui.buttonEggs.setIcon(global_var.app_icon())
            self.ui.buttonEggs.setText("已发现彩蛋: {}".format(len(discovered_eggs)))
        else:
            self.ui.buttonEggs.setVisible(False)

    def show_about(self):
        self.about_cnt += 1
        if self.about_cnt == 10:
            self.find_egg("精力充沛")
        content = "MyRogueLife2\n"
        content += "当前版本号: {}\n".format(global_var.current_version)
        content += "作者: Pitrick"
        if self.about_cnt >= 10:
            content += "\n您真是精力充沛，竟然点了关于界面{}次!".format(self.about_cnt)
        QMessageBox.information(self, "关于", content)

    def show_record(self):
        self.record_cnt += 1
        if self.record_cnt == 10:
            self.find_egg("打破砂锅...")
        if self.record_cnt == 20:
            self.find_egg("...问到底")
        if 20 > self.record_cnt >= 10:
            QMessageBox.warning(self, "不要点了", "确实还没写好，先去体验一下其他的功能(Bug)吧")
        elif self.record_cnt >= 20:
            QMessageBox.critical(self, "不给你点了", "都告诉你没写好了还在这里浪费时间，我决定禁用这个按钮")
            self.ui.buttonRecord.setEnabled(False)
        else:
            QMessageBox.information(self, "对不起", "旅行记录还没有编写完成...")


def init():
    global rlMain
    rlMain = RLMain()


def display() -> None:
    RLDebug.debug("已打开主页面", type='success', who='RLMain')
    rlMain.refresh_egg()
    rlMain.show()


def open_menu():
    # 打开菜单
    if global_var.configs.get_config('enable_debug') is True:
        RLUtility.set_debug_button_visible(True)
    else:
        RLUtility.set_debug_button_visible(False)
    if global_var.configs.get_config('allow_command') is True:
        RLUtility.set_console_button_visible(True)
    else:
        RLUtility.set_console_button_visible(False)
    RLUtility.display()


def quit_program():
    # 弹窗确认是否退出程序
    msgbox = QMessageBox()
    msgbox.setWindowTitle("确认退出")
    msgbox.setText("你确定要退出游戏吗？")
    msgbox.setIcon(QMessageBox.Icon.Question)
    msgbox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    msgbox.setDefaultButton(QMessageBox.StandardButton.Yes)
    msgbox.setButtonText(QMessageBox.StandardButton.Yes, "确定")
    msgbox.setButtonText(QMessageBox.StandardButton.No, "再想想")
    ret = msgbox.exec_()
    if ret == QMessageBox.StandardButton.Yes:
        sys.exit(0)
    else:
        return
