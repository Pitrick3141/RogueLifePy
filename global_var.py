from PySide2.QtGui import QIcon
import RLItems

# 当前版本号，用于检查更新
global current_version

# 程序图标
global _app_icon

# 藏品列表
global items_list

# 玩家信息
global player_info


def init():

    global current_version
    current_version = 'v0.0.1'

    # 读取程序图标
    global _app_icon
    _app_icon = QIcon("ui\\icon.png")

    # 初始化藏品列表
    global items_list
    items_list = {"100001": RLItems.Item(100001, "测试物品1", "测试效果1", "测试描述1", 1)}
    items_list['100001'].addAdjustment('见微知著', 1)

    return


def app_icon():

    # 返回图标
    return _app_icon
