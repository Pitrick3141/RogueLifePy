import os
import time
from threading import Thread

from PySide2.QtUiTools import QUiLoader
from PySide2extn.RoundProgressBar import roundProgressBar

import RLDebug
import RLRescue
import global_var

global rlGame


class RLGame:
    def __init__(self):
        # 加载主窗口UI
        try:
            self.ui = QUiLoader().load(os.path.join('ui', 'FormGame.ui'))
        except RuntimeError:
            # 缺少必要文件，启用恢复模式
            RLRescue.rescueMode()
            self.ui = QUiLoader().load(os.path.join('ui', 'FormGame.ui'))

        # 设置窗口图标
        self.ui.setWindowIcon(global_var.app_icon())

        # 绑定按钮事件
        self.ui.buttonContinue.clicked.connect(self.forward)
        self.ui.buttonReroll.clicked.connect(self.re_roll_dice)
        self.ui.buttonExtra.clicked.connect(self.extra_dice)

        # 检定圆环
        self.progress_check = roundProgressBar(self.ui)
        self.progress_check.setGeometry(810, 70, 100, 100)
        self.progress_check.rpb_setMinimumSize(150, 150)
        self.progress_check.rpb_setMaximumSize(150, 150)
        self.progress_check.rpb_setBarStyle('Hybrid1')
        self.progress_check.rpb_setPathWidth(15)
        self.progress_check.rpb_setLineCap('Circle')
        self.round_progress_reset()

        # 骰子数量
        self.dice_num = 2
        # 骰子成功率
        self.dice_possibility = [[]]

        RLDebug.debug("游戏界面初始化完成", type='success', who=self.__class__.__name__)

    def forward(self):
        self.round_progress_reset()

    def re_roll_dice(self):
        pass

    def extra_dice(self):
        pass

    def set_check_rate(self, current, required):
        self.progress_check.setVisible(True)
        self.ui.labelPossibility.setVisible(True)
        needed = required-current
        total = 6 ** self.dice_num
        possibility = [[35, 35, 35, 35, 33, 30, 26, 21, 15, 10, 6, 3, 1],
                       [215, 215, 215, 215, 215, 212, 206, 196, 181, 160, 135, 108, 81, 56, 35, 20, 10, 4, 1]]
        if needed <= self.dice_num * 6:
            current_possibility = possibility[self.dice_num - 2][needed]
        else:
            current_possibility = 1
        self.progress_check.rpb_setMaximum(total)

        thr = Thread(target=self.round_progress_animate, args=(current_possibility, total))
        thr.start()

        RLDebug.debug("当前已有点数{},需要点数{},检定成功率{}%".format(
            current, required, float(current_possibility)/total*100),
            who=self.__class__.__name__)

    def round_progress_animate(self, target, maximum):
        rate = 1
        value = 0
        while value + rate < target:
            self.progress_check.rpb_setValue(round(value + rate))
            value += rate
            time.sleep(0.03)
            self.update_round_progress(value + rate, maximum)
        self.progress_check.rpb_setValue(target)
        self.update_round_progress(value + rate, maximum)

    def update_round_progress(self, value, maximum):
        if float(value) / maximum >= 0.95:
            self.progress_check.rpb_setLineColor((0, 204, 204))
            self.progress_check.rpb_setTextColor((0, 204, 204))
            self.progress_check.rpb_setPathColor((204, 255, 255))
            self.ui.labelPossibility.setText("几乎必然成功")
            self.ui.labelPossibility.setStyleSheet("QLabel { color : rgb(0, 204, 204); }")
        elif float(value) / maximum >= 0.75:
            self.progress_check.rpb_setLineColor((0, 153, 0))
            self.progress_check.rpb_setTextColor((0, 153, 0))
            self.progress_check.rpb_setPathColor((204, 255, 204))
            self.ui.labelPossibility.setText("成功几率高")
            self.ui.labelPossibility.setStyleSheet("QLabel { color : rgb(0, 153, 0); }")
        elif float(value) / maximum >= 0.55:
            self.progress_check.rpb_setLineColor((204, 204, 0))
            self.progress_check.rpb_setTextColor((204, 204, 0))
            self.progress_check.rpb_setPathColor((255, 255, 204))
            self.ui.labelPossibility.setText("成功几率较高")
            self.ui.labelPossibility.setStyleSheet("QLabel { color : rgb(204, 204, 0); }")
        elif float(value) / maximum >= 0.35:
            self.progress_check.rpb_setLineColor((255, 128, 0))
            self.progress_check.rpb_setTextColor((255, 128, 0))
            self.progress_check.rpb_setPathColor((255, 229, 204))
            self.ui.labelPossibility.setText("成功几率中")
            self.ui.labelPossibility.setStyleSheet("QLabel { color : rgb(255, 128, 0); }")
        elif float(value) / maximum >= 0.05:
            self.progress_check.rpb_setLineColor((204, 0, 0))
            self.progress_check.rpb_setTextColor((204, 0, 0))
            self.progress_check.rpb_setPathColor((255, 204, 204))
            self.ui.labelPossibility.setText("成功几率低")
            self.ui.labelPossibility.setStyleSheet("QLabel { color : rgb(204, 0, 0); }")
        else:
            self.progress_check.rpb_setLineColor((153, 0, 153))
            self.progress_check.rpb_setTextColor((153, 0, 153))
            self.progress_check.rpb_setPathColor((255, 204, 255))
            self.ui.labelPossibility.setText("几乎必然失败")
            self.ui.labelPossibility.setStyleSheet("QLabel { color : rgb(153, 0, 153); }")

    def round_progress_reset(self):
        self.progress_check.setVisible(False)
        self.ui.labelPossibility.setVisible(False)
        self.progress_check.rpb_setValue(0)
        self.progress_check.rpb_setMaximum(100)


def init():
    global rlGame
    rlGame = RLGame()


def display() -> None:
    RLDebug.debug("已打开游戏页面", type='success', who='RLGame')
    rlGame.ui.show()
