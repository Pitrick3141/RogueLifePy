import json
import os
import sys
import time

from PySide2.QtWidgets import QMessageBox
from PySide2.QtUiTools import QUiLoader

import RLGame
import RLRescue
import RLDebug
import RLUtility
import global_var

global rlMain


class RLMain:

    def __init__(self):
        # 加载主窗口UI
        try:
            self.ui = QUiLoader().load(os.path.join('ui', 'FormMain.ui'))
        except RuntimeError:
            # 缺少必要文件，启用恢复模式
            RLRescue.rescue_mode()
            self.ui = QUiLoader().load(os.path.join('ui', 'FormMain.ui'))

        # 设置窗口图标
        self.ui.setWindowIcon(global_var.app_icon())

        # 彩蛋按钮
        self.refresh_egg()

        # 绑定按钮事件
        self.ui.buttonQuit.clicked.connect(quit_program)
        self.ui.buttonEggs.clicked.connect(self.show_eggs)
        self.ui.buttonMenu.clicked.connect(open_menu)
        self.ui.buttonStart.clicked.connect(open_game)

        RLDebug.debug("主界面初始化完成", type='success', who=self.__class__.__name__)

    def show_eggs(self):
        discovered_eggs = global_var.configs.get_config('discovered_eggs')
        eggs_list = ""
        for key in discovered_eggs.keys():
            eggs_list += "【{}】 发现时间: {}\n".format(key, discovered_eggs[key])
        QMessageBox.information(self.ui, "恭喜你已经找到了{}个彩蛋".format(len(discovered_eggs)), eggs_list)

    def find_egg(self, title):
        if 'discovered_eggs' not in global_var.configs.config_keys():
            global_var.configs.set_config('discovered_eggs', {})
        discovered_eggs = global_var.configs.get_config('discovered_eggs')
        if title not in discovered_eggs.keys():
            discovered_eggs[title] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            global_var.configs.set_config('discovered_eggs', discovered_eggs)
        RLDebug.debug("发现了彩蛋【{}】, 总计已发现彩蛋{}个".format(title, len(discovered_eggs)),
                      who=self.__class__.__name__)
        json_dump = {'config': True, 'version': '*', 'discovered_eggs': discovered_eggs}

        # 保存配置文件
        with open(os.path.join('data', 'discovered_eggs.json'), "w") as f:
            json.dump(json_dump, f)
        RLDebug.debug("配置文件已保存至{}".format(os.path.join(os.getcwd(), 'data', 'discovered_eggs.json')),
                      who=self.__class__.__name__)

        # 刷新彩蛋按钮
        self.refresh_egg()

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


def init():
    global rlMain
    rlMain = RLMain()


def display() -> None:
    RLDebug.debug("已打开主页面", type='success', who='RLMain')
    rlMain.ui.show()


def open_menu():
    # 打开菜单
    if global_var.configs.get_config('enable_debug') is True:
        RLUtility.set_debug_button_visible(True)
    else:
        RLUtility.set_debug_button_visible(False)
    RLUtility.display()


def open_game():
    # 打开游戏
    RLGame.display()


def quit_program():
    # 弹窗确认是否退出程序
    msgbox = QMessageBox()
    msgbox.setWindowTitle("确认退出")
    msgbox.setText("你确定要退出游戏吗？")
    msgbox.setIcon(QMessageBox.Question)
    msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msgbox.setDefaultButton(QMessageBox.Yes)
    msgbox.setButtonText(QMessageBox.Yes, "确定")
    msgbox.setButtonText(QMessageBox.No, "再想想")
    ret = msgbox.exec_()
    if ret == QMessageBox.Yes:
        sys.exit(0)
    else:
        return
