from PySide2.QtUiTools import QUiLoader

import RLRescue
import RLDebug
import global_var

global rlConsole


class RLConsole:

    def __init__(self):
        # 加载控制台UI
        try:
            self.ui = QUiLoader().load('ui\\FormConsole.ui')
        except RuntimeError:
            # 缺少必要文件，启用恢复模式
            RLRescue.rescueMode()
            self.ui = QUiLoader().load('ui\\FormConsole.ui')

        # 绑定命令选择框事件
        self.ui.listCommand.itemClicked.connect(self.commandChange)

        # 绑定按钮事件
        self.ui.buttonRun.clicked.connect(self.runCommand)
        self.ui.buttonDebug.clicked.connect(self.showDebug)

        # 绑定输入框事件
        self.ui.lineEditCoef1.textEdited.connect(self.coefficient1Edit)
        self.ui.lineEditCoef2.textEdited.connect(self.coefficient2Edit)

        self.current_command_index = -1
        self.coefficient_1 = 0
        self.coefficient_2 = 0

        # 命令列表
        self.commands_list = ['获取物品', '玩家信息']
        for command in self.commands_list:
            self.ui.listCommand.addItem(command)
        RLDebug.debug("控制台初始化完成", type='success', who=self.__class__.__name__)

    def commandChange(self):
        self.current_command_index = self.ui.listCommand.currentRow()

    def runCommand(self):
        if self.current_command_index == -1:
            RLDebug.debug("请先选择要执行的命令", type='error', who=self.__class__.__name__)
            return
        RLDebug.debug("开始运行序号为{}的命令{}".format(
            self.current_command_index,  self.commands_list[self.current_command_index]),
            who=self.__class__.__name__)
        if self.current_command_index == 0:
            global_var.player_info.attainItem(self.coefficient_1)
        if self.current_command_index == 1:
            global_var.player_info.printPlayerInfo()

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
