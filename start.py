from PySide2.QtWidgets import QApplication

import global_var
import RLDebug
import RLUpdate
# import RLUtility
# import RLMain


# 新建 Pyside2 Application
app = QApplication([])

# 初始化模块
RLDebug.init()
global_var.init()
RLUpdate.init()
# FDCustom.init()
# FDUtility.init()

# 初始化主窗口
# FDMain.init()

# 显示主窗口并导入模板&检查更新
# FDMain.display()
# FDUtility.checkUpdate()
# FDMain.loadTemplates()

# 开始事件循环
# noinspection PyUnboundLocalVariable
app.exec_()

# 窗口关闭后结束Application
del app
