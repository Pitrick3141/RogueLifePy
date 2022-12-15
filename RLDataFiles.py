import hashlib
import json
import os

from PySide2.QtWidgets import QMessageBox, QMainWindow

import RLConfigs
import RLDebug
import RLUtility

global data_files


class DataFiles:

    # 数据文件列表
    _data_files = []

    # 数据文件hash字典，用于同步数据文件
    _data_files_hash = {}

    def __init__(self):
        RLDebug.debug("数据文件模块初始化完成", type='success', who=self.__class__.__name__)

    def loadDataFiles(self):

        self._data_files.clear()
        self._data_files_hash.clear()

        RLDebug.debug("开始载入数据文件...", who=self.__class__.__name__)

        # 若不存在数据文件目录则建立并从云端同步数据文件
        if not os.path.exists("data"):
            QMessageBox.critical(QMainWindow(), "错误",
                                 "数据文件目录不存在或已损坏\n正在建立新的数据文件目录并从云端同步数据文件")
            RLUtility.syncDataFiles()
            return

        # 默认数据文件目录
        data_files_dir = os.walk("data")

        # 遍历数据文件目录
        for path, dir_list, file_list in data_files_dir:
            for file_name in file_list:

                # 检查文件拓展名是否合法
                if not file_name.find(".json") == -1:
                    with open(os.path.abspath(path) + "\\" + file_name, 'rb') as f:
                        # hash
                        data = f.read()
                        hash_obj = hashlib.sha1()
                        hash_str = "blob %u\0" % len(data) + data.decode('utf-8')
                        hash_obj.update(hash_str.encode('utf-8'))
                        hash_value = hash_obj.hexdigest()

                    # 打开数据文件文件
                    with open(os.path.abspath(path) + "\\" + file_name, 'rb') as load_json:

                        # 数据文件文件字典
                        data = {}
                        # 缺少的键值对
                        missed_keys = []
                        # 显示的相对路径名称
                        display_name = path + "\\" + file_name

                        # 尝试读取数据文件文件并转换为字典
                        try:
                            original_data = json.load(load_json)

                        # 解码失败异常：一般是内容为空或者不合法
                        except json.decoder.JSONDecodeError:
                            RLDebug.debug(
                                "已损坏的数据文件：{0}, 数据文件内容为空或不合法, 跳过当前数据文件".format(display_name),
                                type='error', who=self.__class__.__name__)
                            continue
                        except UnicodeDecodeError:
                            RLDebug.debug(
                                "已损坏的数据文件：{0}, 数据文件编码格式有误, 跳过当前数据文件".format(display_name),
                                type='error', who=self.__class__.__name__)
                            continue

                        # 将键全部转换为小写，避免大小写混淆
                        for key, value in original_data.items():
                            data[key.lower()] = value

                        # 检测是否有缺失的必需键值对
                        for checked_key in ['version', 'type']:
                            if checked_key not in data.keys():
                                missed_keys.append(checked_key)

                        # 如果有缺失的关键键值对
                        if not len(missed_keys) == 0:
                            RLDebug.debug("已损坏的数据文件：{0}, 缺失如下键值对:{1}, 跳过当前数据文件".format(
                                display_name,
                                missed_keys)
                                , type='error', who=self.__class__.__name__)
                            continue

                        # 检测是否已经添加了相同的数据文件
                        elif hash_value in self._data_files_hash:
                            RLDebug.debug("已经载入相同的数据文件: {0}, 跳过当前数据文件".format(
                                self._data_files_hash.get(hash_value))
                                , type='warn', who=self.__class__.__name__)
                            continue

                        self._data_files_hash[hash_value] = data.get('name')

                        # 检测是否是配置文件
                        if data.get('type') == 'config':
                            RLDebug.debug("发现配置文件：{0}, 开始解析".format(display_name),
                                          who=self.__class__.__name__)
                            RLConfigs.configs.applyConfig(data)
                            continue

                        # 将数据文件添加到数据文件列表中
                        self._data_files.append(data)

                    RLDebug.debug("已载入数据文件: " + data.get('name'), who=self.__class__.__name__)

                # 文件拓展名不为.json
                else:
                    RLDebug.debug("不支持的文件类型(目前仅支持.json格式)：{0}, 跳过当前数据文件".format(display_name),
                                  type='error', who=self.__class__.__name__)

        RLDebug.debug("数据文件载入完成,共载入{0}个数据文件".format(len(self._data_files))
                      , type='success', who=self.__class__.__name__)

    def data_files_hash_keys(self):
        return self._data_files_hash.keys()

    def data_files_hash_values(self):
        return self._data_files_hash.values()

    def get_data_files_hash(self, key):
        return self._data_files_hash.get(key)

    def set_data_files_hash(self, key, value):
        self._data_files_hash[key] = value
        return

    def data_files_clear(self):
        self._data_files.clear()
        return

    def data_files_hash_clear(self):
        self._data_files_hash.clear()
        return

    def data_files_append(self, value):
        self._data_files.append(value)
        return

    def get_data_files(self, value):
        return self._data_files[value]

    def len_data_files(self):
        return len(self._data_files)


def init():
    global data_files
    data_files = DataFiles()


def loadDataFiles():
    data_files.loadDataFiles()
