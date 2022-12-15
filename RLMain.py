import json
import os
import sys
import time

from PySide2.QtWidgets import QMessageBox
from PySide2.QtUiTools import QUiLoader

import RLRescue
import RLDebug
import RLUtility
import global_var
import RLConfigs

global rlMain


class RLMain:

    def __init__(self):
        # 加载主窗口UI
        try:
            self.ui = QUiLoader().load('ui\\FormMain.ui')
        except RuntimeError:
            # 缺少必要文件，启用恢复模式
            RLRescue.rescueMode()
            self.ui = QUiLoader().load('ui\\FormMain.ui')

        # 设置窗口图标
        self.ui.setWindowIcon(global_var.app_icon())

        # 彩蛋按钮
        self.refreshEgg()

        # 绑定按钮事件
        self.ui.buttonQuit.clicked.connect(self.quitProgram)
        self.ui.buttonEggs.clicked.connect(self.showEggs)
        self.ui.buttonMenu.clicked.connect(self.openMenu)

        RLDebug.debug("主界面初始化完成", type='success')

    def showEggs(self):
        discovered_eggs = RLConfigs.configs.get_config('discovered_eggs')
        eggs_list = ""
        for key in discovered_eggs.keys():
            eggs_list += "【{}】 发现时间: {}\n".format(key, discovered_eggs[key])
        QMessageBox.information(self.ui, "恭喜你已经找到了{}个彩蛋".format(len(discovered_eggs)), eggs_list)

    def findEgg(self, title):
        if 'discovered_eggs' not in RLConfigs.configs.config_keys():
            RLConfigs.configs.set_config('discovered_eggs', {})
        discovered_eggs = RLConfigs.configs.get_config('discovered_eggs')
        if title not in discovered_eggs.keys():
            discovered_eggs[title] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            RLConfigs.configs.set_config('discovered_eggs', discovered_eggs)
        RLDebug.debug("发现了彩蛋【{}】, 总计已发现彩蛋{}个".format(title, len(discovered_eggs)))
        json_dump = {'config': True, 'version': '*', 'discovered_eggs': discovered_eggs}

        # 保存配置文件
        with open("data\\discovered_eggs.json", "w") as f:
            json.dump(json_dump, f)
        RLDebug.debug("配置文件已保存至{}\\{}".format(os.getcwd(), "data\\discovered_eggs.json"))

        # 刷新彩蛋按钮
        self.refreshEgg()

    def refreshEgg(self):
        discovered_eggs = RLConfigs.configs.get_config('discovered_eggs')
        if len(discovered_eggs) > 0:
            self.ui.buttonEggs.setVisible(True)
            self.ui.buttonEggs.setIcon(global_var.app_icon())
            self.ui.buttonEggs.setText("已发现彩蛋: {}".format(len(discovered_eggs)))
        else:
            self.ui.buttonEggs.setVisible(False)

    @staticmethod
    def openMenu():
        # 打开菜单
        if RLConfigs.configs.get_config('enable_debug') is True:
            RLUtility.set_debug_button_visible(True)
        else:
            RLUtility.set_debug_button_visible(False)
        RLUtility.display()

    @staticmethod
    def quitProgram():
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


def init():
    global rlMain
    rlMain = RLMain()


def display() -> None:
    RLDebug.debug("已打开主页面", type='success')
    rlMain.ui.show()
