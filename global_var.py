from PySide2.QtGui import QIcon

# 当前版本号，用于检查更新
current_version = 'v0.0.1'

# 程序图标
global _app_icon

# 配置项字典
global _configs

# 数据文件列表
global _data_files

# 数据文件hash字典，用于同步数据文件
global _data_files_hash


def init():

    # 初始化配置项
    global _configs
    _configs = {}

    # 读取程序图标
    global _app_icon
    _app_icon = QIcon("ui\\icon.png")

    return


def set_config(key, value):

    # 设置配置项
    _configs[key] = value
    return


def get_config(key):

    # 获取配置项
    return _configs.get(key)


def config_keys():

    # 取得配置项键表
    return _configs.keys()


def app_icon():

    # 返回图标
    return _app_icon


def data_files_hash_keys():
    return _data_files_hash.keys()


def data_files_hash_values():
    return _data_files_hash.values()


def get_data_files_hash(key):
    return _data_files_hash.get(key)


def set_data_files_hash(key, value):
    _data_files_hash[key] = value
    return


def data_files_hash_clear():
    _data_files_hash.clear()
    return


def data_files_append(value):
    _data_files.append(value)
    return


def get_data_files(value):
    return _data_files[value]


def len_data_files():
    return len(_data_files)


def data_files_clear():
    _data_files.clear()
    return
