import platform
import os
from PySide2.QtWidgets import QApplication

# 导入模块
import RLPlayer

import global_var
import RLDebug
import RLConfigs
import RLDataFiles
import RLUpdate
import RLUtility
import RLMain

import RLConsole


# 新建 Pyside2 Application
app = QApplication([])

if 'mac' in platform.platform().lower():
    os.environ['QT_MAC_WANTS_LAYER'] = '1'

# 初始化模块
global_var.init()

RLDebug.init()
RLConfigs.init()


RLPlayer.init()

RLUpdate.init()
RLUtility.init()

# 载入数据文件
RLDataFiles.load_data_files()

# 初始化主窗口
RLMain.init()

# 初始化命令台
RLConsole.init()

# 显示主窗口&检查更新

RLMain.display()
# RLUtility.checkUpdate()

# 开始事件循环
# noinspection PyUnboundLocalVariable
app.exec_()

# 窗口关闭后结束Application
del app
