import hashlib
import json
import os
import time

from PySide2.QtWidgets import QMessageBox, QMainWindow

import RLDebug
import RLItems
import RLPlayer
import RLUtility
import global_var


def load_data_files():
    global_var.data_files.clear()
    global_var.data_files_hash.clear()

    RLDebug.debug("开始载入数据文件...", who='DataFiles')

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
                with open(os.path.join(path, file_name), 'rb') as f:
                    # hash
                    data = f.read()
                    hash_obj = hashlib.sha1()
                    hash_str = "blob %u\0" % len(data) + data.decode('utf-8')
                    hash_obj.update(hash_str.encode('utf-8'))
                    hash_value = hash_obj.hexdigest()

                # 打开数据文件文件
                with open(os.path.join(path, file_name), 'rb') as load_json:

                    # 数据文件文件字典
                    data = {}
                    # 缺少的键值对
                    missed_keys = []
                    # 显示的相对路径名称
                    display_name = os.path.join(path, file_name)

                    # 尝试读取数据文件文件并转换为字典
                    try:
                        original_data = json.load(load_json)

                    # 解码失败异常：一般是内容为空或者不合法
                    except json.decoder.JSONDecodeError:
                        RLDebug.debug(
                            "已损坏的数据文件：{0}, 数据文件内容为空或不合法, 跳过当前数据文件".format(display_name),
                            type='error', who='DataFiles')
                        continue
                    except UnicodeDecodeError:
                        RLDebug.debug(
                            "已损坏的数据文件：{0}, 数据文件编码格式有误, 跳过当前数据文件".format(display_name),
                            type='error', who='DataFiles')
                        continue

                    # 将键全部转换为小写，避免大小写混淆
                    for key, value in original_data.items():
                        data[key.lower()] = value

                    # 检测是否有缺失的必需键值对
                    for checked_key in ['name', 'version', 'type']:
                        if checked_key not in data.keys():
                            missed_keys.append(checked_key)

                    # 如果有缺失的关键键值对
                    if not len(missed_keys) == 0:
                        RLDebug.debug("已损坏的数据文件：{0}, 缺失如下键值对:{1}, 跳过当前数据文件".format(
                            display_name,
                            missed_keys),
                            type='error', who='DataFiles')
                        continue

                    # 检测是否已经添加了相同的数据文件
                    elif hash_value in global_var.data_files_hash:
                        RLDebug.debug("已经载入相同的数据文件: {0}, 跳过当前数据文件".format(
                            global_var.data_files_hash.get(hash_value)),
                            type='warn', who='DataFiles')
                        continue

                    global_var.data_files_hash[hash_value] = data.get('name')
                    global_var.data_files.append(data)
                    # 将数据文件添加到数据文件列表中

                    # 检测是否是配置文件
                    if data.get('type') == 'config':
                        RLDebug.debug("发现配置文件：{0}, 开始解析".format(display_name),
                                      who='DataFiles')
                        global_var.configs.applyConfig(data)

                    # 检测是否是物品数据文件
                    if data.get('type') == 'item':
                        RLDebug.debug("发现物品数据文件：{0}, 开始解析".format(display_name),
                                      who='DataFiles')
                        RLItems.load_items(data)

                    # 检测是否是玩家信息存档文件
                    if data.get('type') == 'player':
                        RLDebug.debug("发现玩家信息存档文件：{0}, 开始解析".format(display_name),
                                      who='DataFiles')
                        RLPlayer.load_player_info(data)

                RLDebug.debug("已载入数据文件: " + data.get('name'), who='DataFiles')

            # 文件拓展名不为.json
            else:
                RLDebug.debug("不支持的文件类型(目前仅支持.json格式)：{0}, 跳过当前数据文件".format(display_name),
                              type='error', who='DataFiles')

    RLDebug.debug("数据文件载入完成,共载入{0}个数据文件".format(len(global_var.data_files)),
                  type='success', who='DataFiles')


def save_player_info():
    if not os.path.exists(os.path.join('data', 'save')):
        os.mkdir(os.path.join('data', 'save'))

    save_name = os.path.join(os.getcwd(), 'data', 'save', 'save.json')

    # 检测存档是否存在
    if os.path.exists(os.path.join('data', 'save', 'save.json')):
        # 弹窗确认是否覆盖保存
        msgbox = QMessageBox()
        msgbox.setWindowTitle("存档已存在")
        msgbox.setText("你确定要覆盖当前存档吗？")
        msgbox.setInformativeText("当前同名模板:{}".format(os.path.join(os.getcwd(), 'data', 'save', 'save.json')))
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.Ok | QMessageBox.No)
        msgbox.setDefaultButton(QMessageBox.Yes)
        msgbox.setButtonText(QMessageBox.Yes, "覆盖保存")
        msgbox.setButtonText(QMessageBox.Ok, "重命名保存")
        msgbox.setButtonText(QMessageBox.No, "取消保存")
        ret = msgbox.exec_()
        if ret == QMessageBox.Ok:
            save_name = os.path.join('data', 'save', 'save_{}.json'.format(time.strftime(
                "%Y_%m_%d_%H_%M_%S", time.localtime())))
        elif ret == QMessageBox.Yes:
            save_name = os.path.join('data', 'save', 'save.json')
        else:
            return

    player = global_var.player_info
    # 处理json字典
    json_dump = {"name": "save_{}".format(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())),
                 "version": global_var.current_version,
                 "type": "player",
                 "player": {
                     "adjustments": player.adjustments,
                     "attained_items": player.attained_items
                 }}

    # 保存json文件
    with open(save_name, "w") as f:
        json.dump(json_dump, f)

    QMessageBox.information(QMainWindow(),
                            "保存成功",
                            "玩家信息已保存至{}".format(os.path.join(os.getcwd(), save_name)),
                            QMessageBox.Ok)
    RLDebug.debug("玩家信息已保存至{}".format(os.path.join(os.getcwd(), save_name)),
                  type='success', who='DataFiles')


def reformat_data_file(file_name):
    file_path = os.path.join('data', file_name)
    # 打开数据文件文件
    with open(file_path, 'rb') as load_json:

        # 数据文件文件字典
        data = {}
        # 缺少的键值对
        missed_keys = []
        # 显示的相对路径名称
        display_name = file_path

        # 尝试读取数据文件文件并转换为字典
        try:
            original_data = json.load(load_json)

        # 解码失败异常：一般是内容为空或者不合法
        except json.decoder.JSONDecodeError:
            RLDebug.debug(
                "已损坏的数据文件：{0}, 数据文件内容为空或不合法, 跳过当前数据文件".format(display_name),
                type='error', who='DataFiles')
            return
        except UnicodeDecodeError:
            RLDebug.debug(
                "已损坏的数据文件：{0}, 数据文件编码格式有误, 跳过当前数据文件".format(display_name),
                type='error', who='DataFiles')
            return

        # 将键全部转换为小写，避免大小写混淆
        for key, value in original_data.items():
            data[key.lower()] = value

        # 检测是否有缺失的必需键值对
        for checked_key in ['name', 'version', 'type']:
            if checked_key not in data.keys():
                missed_keys.append(checked_key)

        # 如果有缺失的关键键值对
        if not len(missed_keys) == 0:
            RLDebug.debug("已损坏的数据文件：{0}, 缺失如下键值对:{1}, 跳过当前数据文件".format(
                display_name,
                missed_keys),
                type='error', who='DataFiles')
            return

        save_name = '{}_reformatted.json'.format(data.get('name'))

        with open(os.path.join('data', save_name), "w") as f:
            json.dump(data, f)

        RLDebug.debug("数据文件已重新格式化保存为{}".format(save_name), type='success', who='DataFiles')
