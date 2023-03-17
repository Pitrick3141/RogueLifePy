from PySide6.QtGui import QIcon
import os

# 当前版本号，用于检查更新
global current_version

# 程序图标
global _app_icon

# 藏品列表
global items_list
global items_weight_list
global random_items

# 事件列表
global events_list
global events_weight_list
global random_events

# 挑战列表
global challenges_list

# 行动列表
global actions_list

# 玩家信息
global player_info
global save_name

# 配置项
global configs

# 数据文件列表
global data_files

# 数据文件哈希字典
global data_files_hash


def init():
    global current_version
    current_version = 'v1.0.1'

    # 读取程序图标
    global _app_icon
    _app_icon = QIcon(os.path.join('ui', 'icon.ico'))

    # 初始化藏品列表
    global items_list
    items_list = {}
    global items_weight_list
    items_weight_list = {}
    global random_items
    random_items = None

    # 初始化事件列表
    global events_list
    events_list = {}
    global events_weight_list
    events_weight_list = {}
    global random_events
    random_events = None

    # 初始化挑战列表
    global challenges_list
    challenges_list = {}

    # 初始化行动列表
    global actions_list
    actions_list = {}

    # 初始化配置项
    global configs
    configs = {}

    # 初始化玩家信息
    global player_info
    player_info = None
    global save_name
    save_name = "save"

    # 初始化数据文件
    global data_files
    data_files = []
    global data_files_hash
    data_files_hash = {}

    return


def app_icon():
    # 返回图标
    return _app_icon
