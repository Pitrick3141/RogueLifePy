import os
import platform

from PySide6.QtWidgets import QApplication

# 导入模块
import RLConfigs
import RLConsole
import RLDataFiles
import RLDebug
import RLEditor
import RLGame
import RLMain
import RLPlayer
import RLUpdate
import RLUtility

import global_var

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

# 初始化游戏窗口
RLGame.init()

# 初始化编辑器
RLEditor.init()

# 初始化命令台
RLConsole.init()

# 加载完成计时
RLDebug.loaded()

# 显示主窗口&检查更新
RLMain.display()
RLUtility.check_update()

# 开始事件循环
# noinspection PyUnboundLocalVariable
app.exec()

# 窗口关闭后结束Application
del app
