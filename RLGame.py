import os
import random
import time
from threading import Thread

from PySide2.QtGui import QIcon
from PySide2.QtUiTools import QUiLoader
from PySide2extn.RoundProgressBar import roundProgressBar

import RLConsole
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

        # 绑定选择框事件
        self.ui.checkExtra.stateChanged.connect(self.extra_dice)

        # 绑定菜单事件
        self.ui.actionShowCollections.triggered.connect(self.show_collections)
        self.ui.actionShowAdjustments.triggered.connect(self.show_adjustments)
        self.ui.actionShowCurrentAdjustments.triggered.connect(self.show_current_adjustments)
        self.ui.actionConsole.triggered.connect(self.show_console)

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
        # 投出的骰子
        self.dices = []

        # 设定不可见
        self.ui.labelExtra.setVisible(False)

        RLDebug.debug("游戏界面初始化完成", type='success', who=self.__class__.__name__)

    def forward(self):
        self.round_progress_reset()

    def roll_dice(self, **kwargs):
        self.ui.dice1.setIcon(QIcon())
        self.ui.dice2.setIcon(QIcon())
        self.ui.dice3.setIcon(QIcon())
        self.ui.labelExtra.setVisible(False)
        self.ui.labelRolled.setStyleSheet("")
        self.ui.labelRolled.setText("")
        self.ui.buttonReroll.setEnabled(False)
        self.ui.checkExtra.setEnabled(False)
        if kwargs.get('manipulate') is not None:
            self.dices = [kwargs['manipulate'][0] if 1 <= kwargs['manipulate'][0] <= 6 else random.randint(1, 6),
                          kwargs['manipulate'][1] if 1 <= kwargs['manipulate'][0] <= 6 else random.randint(1, 6),
                          kwargs['manipulate'][2] if 1 <= kwargs['manipulate'][0] <= 6 else random.randint(1, 6)]
        else:
            self.dices = [random.randint(1, 6), random.randint(1, 6)]
        if self.dice_num == 3:
            self.dices.append(random.randint(1, 6))
        thr = Thread(target=self.dice_animate)
        thr.start()

    def dice_animate(self):
        dice_interval = 0.1
        dice_repeat = [random.randint(5, 15), random.randint(5, 15)]
        repeat_max = max(dice_repeat[0], dice_repeat[1])
        for i in range(repeat_max + 1):
            if dice_repeat[0] > i:
                dice1_img = random.randint(1, 6)
                self.ui.dice1.setIcon(QIcon(os.path.join('ui', 'dices', 'inverted-dice-{}.png'.format(dice1_img))))
            else:
                self.ui.dice1.setIcon(QIcon(os.path.join('ui', 'dices', 'inverted-dice-{}.png'.format(self.dices[0]))))
            if dice_repeat[1] > i:
                dice2_img = random.randint(1, 6)
                self.ui.dice2.setIcon(QIcon(os.path.join('ui', 'dices', 'inverted-dice-{}.png'.format(dice2_img))))
            else:
                self.ui.dice2.setIcon(QIcon(os.path.join('ui', 'dices', 'inverted-dice-{}.png'.format(self.dices[1]))))
            time.sleep(dice_interval)
        time.sleep(dice_interval * 5)
        if self.dices[0] == 6 and self.dices[1] == 6:
            self.ui.dice1.setIcon(QIcon(os.path.join('ui', 'dices', 'dice-6-green.png')))
            self.ui.dice2.setIcon(QIcon(os.path.join('ui', 'dices', 'dice-6-green.png')))
        elif self.dices[0] == 1 and self.dices[1] == 1:
            self.ui.dice1.setIcon(QIcon(os.path.join('ui', 'dices', 'dice-1-red.png')))
            self.ui.dice2.setIcon(QIcon(os.path.join('ui', 'dices', 'dice-1-red.png')))
        else:
            self.ui.dice1.setIcon(QIcon(os.path.join('ui', 'dices', 'dice-{}.png'.format(self.dices[0]))))
            self.ui.dice2.setIcon(QIcon(os.path.join('ui', 'dices', 'dice-{}.png'.format(self.dices[1]))))

        if self.dice_num == 3:
            self.ui.labelExtra.setVisible(True)
            for i in range(random.randint(10, 20)):
                dice3_img = random.randint(1, 6)
                self.ui.dice3.setIcon(QIcon(os.path.join('ui', 'dices', 'inverted-dice-{}.png'.format(dice3_img))))
                time.sleep(dice_interval)
            self.ui.dice3.setIcon(QIcon(os.path.join('ui', 'dices', 'inverted-dice-{}.png'.format(self.dices[2]))))
            time.sleep(dice_interval * 5)
            self.ui.dice3.setIcon(QIcon(os.path.join('ui', 'dices', 'dice-{}.png'.format(self.dices[2]))))
        if self.dices[0] == 6 and self.dices[1] == 6:
            self.ui.labelRolled.setStyleSheet("background-color: green")
            self.ui.labelRolled.setText("骰子大成功")
        elif self.dices[0] == 1 and self.dices[1] == 1:
            self.ui.labelRolled.setStyleSheet("background-color: red")
            self.ui.labelRolled.setText("骰子大失败")
        elif self.dice_num == 3:
            self.ui.labelRolled.setText("骰子点数: {} + {} + {}(额外骰子) = {}"
                                        .format(self.dices[0],
                                                self.dices[1],
                                                self.dices[2],
                                                self.dices[0] + self.dices[1] + self.dices[2]))
        else:
            self.ui.labelRolled.setText("骰子点数: {} + {} = {}"
                                        .format(self.dices[0],
                                                self.dices[1],
                                                self.dices[0] + self.dices[1]))
        self.ui.buttonReroll.setEnabled(True)
        self.ui.checkExtra.setEnabled(True)

    def re_roll_dice(self):
        self.roll_dice()

    def extra_dice(self):
        if self.ui.checkExtra.isChecked():
            self.dice_num = 3
        else:
            self.dice_num = 2

    def set_check_rate(self, current, required):
        self.ui.labelRequired.setText("需求点数: {}".format(required))
        self.ui.labelPossessed.setText("已有点数: {}".format(current))
        self.progress_check.setVisible(True)
        self.ui.labelPossibility.setVisible(True)
        needed = required-current
        total = 6 ** self.dice_num
        current_possibility = 0
        possibility = [[35, 35, 35, 35, 33, 30, 26, 21, 15, 10, 6, 3, 1],
                       [215, 215, 215, 215, 215, 212, 206, 196, 181, 160, 135, 108, 81, 56, 35, 20, 10, 4, 1]]
        if needed <= 0:
            current_possibility = total * 35 / 36
        elif needed <= self.dice_num * 6:
            current_possibility = possibility[self.dice_num - 2][needed]
        if current_possibility < total / 36 or needed > self.dice_num * 6:
            current_possibility = total / 36
        self.progress_check.rpb_setMaximum(total)

        thr = Thread(target=self.round_progress_animate, args=(current_possibility,))
        thr.start()

        self.update_round_progress(current_possibility, total)

        RLDebug.debug("当前已有点数{},需要点数{},检定成功率{}%".format(
            current, required, float(current_possibility)/total*100),
            who=self.__class__.__name__)

    def round_progress_animate(self, target):
        rate = 1
        if self.dice_num == 3:
            rate = 6
        value = 0
        animate_interval = 0.03
        while value + rate < target:
            self.progress_check.rpb_setValue(round(value + rate))
            value += rate
            time.sleep(animate_interval)
        self.progress_check.rpb_setValue(target)

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

    def show_collections(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def show_adjustments(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def show_current_adjustments(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    @staticmethod
    def show_console():
        # 显示控制台
        RLConsole.display()


def init():
    global rlGame
    rlGame = RLGame()


def display() -> None:
    RLDebug.debug("已打开游戏页面", type='success', who='RLGame')
    rlGame.ui.show()
