import time
import os

from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QMainWindow

import global_var
from ui.ui_form_debug import Ui_FormDebug

global rlDebug


class RLDebug(QMainWindow):

    def __init__(self):

        # 加载调试窗口UI
        super(RLDebug, self).__init__()
        self.ui = Ui_FormDebug()
        self.ui.setupUi(self)

        self.enable_file_output = False
        self.output_file = None

        # 输出加载时间
        self.debug("", split=2)
        self.debug("开始加载游戏，当前时间戳{}".format(round(global_var.start_time)), type='info', who='RLDebug')

        if os.path.isfile("debug_output.log"):
            self.enable_file_output = True
            self.output_file = open(r"debug_output.log", 'a+')
            self.debug("调试信息文件输出已启用", type='info', who=self.__class__.__name__)

        self.debug("调试输出模块初始化完成", type='success', who=self.__class__.__name__)

    def debug(self, text: str, **kwargs) -> None:

        # 读取当前时间
        current_time = time.strftime("%H:%M:%S", time.localtime())

        # 处理传入参数

        # 分割线
        if kwargs.get('split'):
            # 将调试信息输出
            self.ui.textDebug.append("——" * kwargs.get('split') * 5)
            # 移动到文本框底部
            self.ui.textDebug.moveCursor(QTextCursor.MoveOperation.End)
            print("-" * kwargs.get('split') * 5)
            return

        # 信息来源
        info_sources = {'RLMain': '@主界面',
                        'RLUpdate': '@更新检查实用工具',
                        'RLMenu': '@功能菜单',
                        'RLDebug': '@调试输出',
                        'Configs': '@配置项模块',
                        'DataFiles': '@数据文件模块',
                        'RLConsole': '@控制台',
                        'Player': '@玩家信息',
                        'Items': '@藏品信息',
                        'Conditions': '@检定模块',
                        'RLGame': '@游戏界面',
                        'Events': '@事件信息',
                        'Challenges': '@挑战信息',
                        'Actions': '@行动信息',
                        'WeightedRandom': '@随机数生成器',
                        'RLEditor': '@编辑器',
                        }

        info_from = "@未知来源"
        if kwargs.get('who'):
            who = kwargs.get('who')
            if who in info_sources:
                info_from = info_sources[who]
            else:
                info_from = '@' + who

        # 错误信息
        if kwargs.get('type') == 'error':
            prefix = "<b style=\"color:Red;\">"
            suffix = "</b>"
            output_message = " [Error{}] {}".format(info_from, text)
        # 警告信息
        elif kwargs.get('type') == 'warn':
            prefix = "<span style=\"color:Orange;\">"
            suffix = "</span>"
            output_message = " [Warn{}] {}".format(info_from, text)
        # 成功信息
        elif kwargs.get('type') == 'success':
            prefix = "<span style=\"color:YellowGreen;\">"
            suffix = "</span>"
            output_message = " [Success{}] {}".format(info_from, text)
        # 其他信息
        else:
            prefix = "<span>"
            suffix = "</span>"
            output_message = " [Info{}] {}".format(info_from, text)

        # 将调试信息输出
        self.ui.textDebug.append(prefix + current_time + output_message + suffix)
        # 移动到文本框底部
        self.ui.textDebug.moveCursor(QTextCursor.MoveOperation.End)
        # 控制台输出
        print(current_time + output_message)
        # 文件输出
        if self.enable_file_output:
            self.output_file.write(current_time + output_message + '\n')


def init():
    global rlDebug
    rlDebug = RLDebug()


def debug(text: str, **kwargs) -> None:
    rlDebug.debug(text, **kwargs)


def split(length=2):
    rlDebug.debug("", split=length)


def display() -> None:
    debug("已打开调试输出界面", type='success', who='RLDebug')
    rlDebug.show()


def loaded() -> None:
    global_var.loaded()
    # 加载完成
    debug("游戏加载完成，当前时间戳{}，总加载用时{}ms({}s)".format(
        round(global_var.loaded_time),
        round(global_var.time_consumption, 2),
        round(global_var.time_consumption / 1000, 2)
    ), type='success', who='RLDebug')
    split()
