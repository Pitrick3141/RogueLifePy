from PySide2.QtGui import QIcon

# 当前版本号，用于检查更新
global current_version

# 程序图标
global _app_icon


def init():

    global current_version
    current_version = 'v0.0.1'

    # 读取程序图标
    global _app_icon
    _app_icon = QIcon("ui\\icon.png")

    return


def app_icon():

    # 返回图标
    return _app_icon
