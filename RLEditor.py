import RLDebug

from PySide6.QtWidgets import QMainWindow, QMessageBox

import global_var
from ui.ui_form_editor import Ui_FormEditor

global rlEditor


class RLEditor(QMainWindow):
    def __init__(self):
        # 加载编辑器窗口UI
        super(RLEditor, self).__init__()
        self.ui = Ui_FormEditor()
        self.ui.setupUi(self)

        # 绑定按钮事件
        self.ui.buttonRefresh.clicked.connect(self.refresh)

        # 绑定列表框事件
        self.ui.listItems.itemDoubleClicked.connect(self.select_item)
        self.ui.listEvents.itemDoubleClicked.connect(self.select_event)
        self.ui.listActions.itemDoubleClicked.connect(self.select_action)
        self.ui.listChallenges.itemDoubleClicked.connect(self.select_challenge)

        # 复制全局数据文件
        self.items_list = global_var.items_list
        self.events_list = global_var.events_list
        self.challenges_list = global_var.challenges_list
        self.actions_list = global_var.actions_list

        # 序号映射
        self.items_index_list = []
        self.events_index_list = []
        self.challenges_index_list = []
        self.actions_index_list = []

        RLDebug.debug("编辑器初始化完成", type='success', who=self.__class__.__name__)

        self.refresh()

    def refresh(self):
        self.ui.listItems.clear()
        self.ui.listEvents.clear()
        self.ui.listChallenges.clear()
        self.ui.listActions.clear()
        self.ui.lineIndex.clear()
        self.ui.lineName.clear()
        self.ui.textDes.clear()
        self.ui.textEff.clear()
        for index in self.items_list:
            self.ui.listItems.addItem("{} {}".format(self.items_list[index].index, self.items_list[index].name))
            self.items_index_list.append(index)
        for index in self.events_list:
            self.ui.listEvents.addItem("{} {}".format(self.events_list[index].index, self.events_list[index].name))
            self.events_index_list.append(index)
        for index in self.challenges_list:
            self.ui.listChallenges.addItem("{} {}".format(self.challenges_list[index].index, self.challenges_list[index].name))
            self.challenges_index_list.append(index)
        for index in self.actions_list:
            self.ui.listActions.addItem("{} {}".format(self.actions_list[index].index, self.actions_list[index].name))
            self.actions_index_list.append(index)

    def select_change(self, selected_type):
        self.clear_edit_zone()
        """
        Types of selected
        
        item
        event
        action
        challenge
        
        """
        self.ui.tabResults.setEnabled(selected_type in ['challenge', 'event'])
        self.ui.tabPossibility.setEnabled(selected_type in ['item', 'event'])
        self.ui.tabAdjustment.setEnabled(selected_type in ['item', 'challenge'])
        self.ui.frameRequiredAdjustment.setEnabled(selected_type == 'challenge')
        self.ui.tabBind.setEnabled(selected_type == 'event')
        self.ui.tabAction.setEnabled(selected_type == 'action')
        self.ui.tabEdit.setCurrentIndex(0)

    def select_item(self):
        self.select_change('item')
        selected_index = self.items_index_list[self.ui.listItems.currentRow()]
        self.ui.lineIndex.setText(str(selected_index))
        self.ui.lineName.setText(self.items_list[selected_index].name)
        self.ui.textDes.appendPlainText(self.items_list[selected_index].des)
        self.ui.textEff.appendPlainText(self.items_list[selected_index].eff)

    def select_event(self):
        self.select_change('event')
        selected_index = self.events_index_list[self.ui.listEvents.currentRow()]
        self.ui.lineIndex.setText(str(selected_index))
        self.ui.lineName.setText(self.events_list[selected_index].name)
        self.ui.textDes.appendPlainText(self.events_list[selected_index].des)
        self.ui.textEff.appendPlainText(self.events_list[selected_index].eff)

    def select_action(self):
        self.select_change('action')
        selected_index = self.actions_index_list[self.ui.listActions.currentRow()]
        self.ui.lineIndex.setText(str(selected_index))
        self.ui.lineName.setText(self.actions_list[selected_index].name)
        self.ui.textDes.appendPlainText(self.actions_list[selected_index].des)
        self.ui.textEff.appendPlainText(self.actions_list[selected_index].eff)

    def select_challenge(self):
        self.select_change('challenge')
        selected_index = self.challenges_index_list[self.ui.listChallenges.currentRow()]
        self.ui.lineIndex.setText(str(selected_index))
        self.ui.lineName.setText(self.challenges_list[selected_index].name)
        self.ui.textDes.appendPlainText(self.challenges_list[selected_index].des)
        self.ui.textEff.appendPlainText(self.challenges_list[selected_index].eff)

    def clear_edit_zone(self):
        self.ui.lineName.clear()
        self.ui.textDes.clear()
        self.ui.textEff.clear()


def init():
    global rlEditor
    rlEditor = RLEditor()


def display() -> None:
    RLDebug.debug("已打开编辑器", type='success', who='RLEditor')
    rlEditor.show()
