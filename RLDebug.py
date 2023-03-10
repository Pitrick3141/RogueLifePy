import time
import os
from PySide2.QtUiTools import QUiLoader

import RLRescue

global rlDebug


class RLDebug:

    def __init__(self):
        # 加载调试窗口UI
        try:
            self.ui = QUiLoader().load(os.path.join('ui', 'FormDebug.ui'))
        except RuntimeError:
            # 缺少必要文件，启用恢复模式
            RLRescue.rescue_mode()
            self.ui = QUiLoader().load(os.path.join('ui', 'FormDebug.ui'))
        self.debug("调试输出模块初始化完成", type='success', who=self.__class__.__name__)

    def debug(self, text: str, **kwargs) -> None:
        # 读取当前时间
        current_time = time.strftime("%H:%M:%S", time.localtime())

        # 处理传入参数

        # 分割线
        if kwargs.get('split'):
            # 将调试信息输出
            self.ui.textDebug.append("-" * kwargs.get('split') * 5)
            # 移动到文本框底部
            self.ui.textDebug.moveCursor(self.ui.textDebug.textCursor().End)
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
        self.ui.textDebug.moveCursor(self.ui.textDebug.textCursor().End)
        print(current_time + output_message)


def init():
    global rlDebug
    rlDebug = RLDebug()


def debug(text: str, **kwargs) -> None:
    rlDebug.debug(text, **kwargs)


def split(length=2):
    rlDebug.debug("", split=length)


def display() -> None:
    debug("已打开调试输出界面", type='success', who='RLDebug')
    rlDebug.ui.show()
