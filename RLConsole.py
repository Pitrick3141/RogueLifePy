from PySide2.QtUiTools import QUiLoader
import os

import RLConditions
import RLDataFiles
import RLGame
import RLRescue
import RLDebug
import global_var

global rlConsole


class RLConsole:

    def __init__(self):
        # 加载控制台UI
        try:
            self.ui = QUiLoader().load(os.path.join('ui', 'FormConsole.ui'))
        except RuntimeError:
            # 缺少必要文件，启用恢复模式
            RLRescue.rescueMode()
            self.ui = QUiLoader().load(os.path.join('ui', 'FormConsole.ui'))

        # 绑定命令选择框事件
        self.ui.listCommand.itemClicked.connect(self.commandChange)

        # 绑定按钮事件
        self.ui.buttonRun.clicked.connect(self.runCommand)
        self.ui.buttonDebug.clicked.connect(self.showDebug)

        # 绑定输入框事件
        self.ui.lineEditCoef1.textEdited.connect(self.coefficient1Edit)
        self.ui.lineEditCoef2.textEdited.connect(self.coefficient2Edit)

        # 设定参数
        self.set_coefficient((None, None))

        self.current_command_index = -1
        self.coefficient_1 = ""
        self.coefficient_2 = ""

        # 命令列表
        self.commands_list = ['获取物品',
                              '玩家信息',
                              '设置修正',
                              '保存玩家信息',
                              '格式化数据文件',
                              '判断基本语句',
                              '判断复合语句',
                              '测试复合语句拆分',
                              '游戏页面成功率测试']
        self.coefficients_list = [('物品序号', None),
                                  (None, None),
                                  ("修正名称", "修正值"),
                                  (None, None),
                                  ('文件名', None),
                                  ('语句', None),
                                  ('语句', None),
                                  ('语句', None),
                                  ('当前', '需要'),
                                  ]
        for command in self.commands_list:
            self.ui.listCommand.addItem(command)
        RLDebug.debug("控制台初始化完成", type='success', who=self.__class__.__name__)

    def commandChange(self):
        self.ui.lineEditCoef1.clear()
        self.ui.lineEditCoef2.clear()
        self.current_command_index = self.ui.listCommand.currentRow()
        self.set_coefficient(self.coefficients_list[self.current_command_index])

    def set_coefficient(self, coefficients):
        (coefficient_1, coefficient_2) = coefficients
        if coefficient_1 is None:
            self.ui.lineEditCoef1.setVisible(False)
            self.ui.labelCoef1.setVisible(False)
        else:
            self.ui.lineEditCoef1.setVisible(True)
            self.ui.labelCoef1.setVisible(True)
            self.ui.labelCoef1.setText(coefficient_1)
        if coefficient_2 is None:
            self.ui.lineEditCoef2.setVisible(False)
            self.ui.labelCoef2.setVisible(False)
        else:
            self.ui.lineEditCoef2.setVisible(True)
            self.ui.labelCoef2.setVisible(True)
            self.ui.labelCoef2.setText(coefficient_2)

    def runCommand(self):
        if self.current_command_index == -1:
            RLDebug.debug("请先选择要执行的命令", type='error', who=self.__class__.__name__)
            return
        RLDebug.debug("开始运行序号为{}的命令{}".format(
            self.current_command_index,  self.commands_list[self.current_command_index]),
            who=self.__class__.__name__)
        if self.current_command_index == 0:
            global_var.player_info.attainItem(int(self.coefficient_1))
        elif self.current_command_index == 1:
            global_var.player_info.printPlayerInfo()
        elif self.current_command_index == 2:
            global_var.player_info.addAdjustment(self.coefficient_1, int(self.coefficient_2))
        elif self.current_command_index == 3:
            RLDataFiles.save_player_info()
        elif self.current_command_index == 4:
            RLDataFiles.reformat_data_file(self.coefficient_1)
        elif self.current_command_index == 5:
            RLConditions.check_logic(self.coefficient_1)
        elif self.current_command_index == 6:
            if RLConditions.check(RLConditions.parse_conditions(self.coefficient_1)[0]) is True:
                RLDebug.debug("判断完毕，最终结果为真", type='success', who=self.__class__.__name__)
            else:
                RLDebug.debug("判断完毕，最终结果为假", type='success', who=self.__class__.__name__)
        elif self.current_command_index == 7:
            RLConditions.test_parse(RLConditions.parse_conditions(self.coefficient_1)[0], 0)
        elif self.current_command_index == 8:
            RLGame.rlGame.set_check_rate(int(self.coefficient_1), int(self.coefficient_2))

    def coefficient1Edit(self):
        self.coefficient_1 = self.ui.lineEditCoef1.text()

    def coefficient2Edit(self):
        self.coefficient_2 = self.ui.lineEditCoef2.text()

    @staticmethod
    def showDebug():
        # 显示调试输出
        RLDebug.display()


def init():
    global rlConsole
    rlConsole = RLConsole()


def display() -> None:
    RLDebug.debug("已打开控制台", type='success', who='RLConsole')
    rlConsole.ui.show()
