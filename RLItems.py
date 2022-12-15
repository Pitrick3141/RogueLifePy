import RLDebug
from RLCollections import Collections
import global_var


class Item(Collections):
    # 藏品类
    def __init__(self, index: int, name: str, eff: str, des: str, rare: int, exclusive=False):
        super(Item, self).__init__(index, name, eff, des, exclusive)
        # 稀有度
        self.rare = rare
        # 修正
        self.adjustments = {}

    def addAdjustment(self, adjustment: str, value: int):
        # 向藏品添加修正
        if adjustment not in self.adjustments.keys():
            self.adjustments[adjustment] = value
        return


def load_items(item_file):
    # 应用藏品文件
    cnt = 0

    # 检测藏品文件是否启用
    if not item_file.get('enabled') is True:
        RLDebug.debug("藏品文件未被启用或格式错误，跳过本次解析", type='error', who='Items')
        return

    # 检测配置文件版本是否符合
    if not item_file.get('version') in [global_var.current_version, '*', 'all']:
        RLDebug.debug(
            "藏品文件版本不符或格式错误，跳过本次解析<br>当前版本: {}<br>配置文件版本: {}".format(
                global_var.current_version,
                item_file.get('version')),
            type='error', who='Items')
        return

    # 遍历藏品
    for item in item_file.get('items'):
        new_item = Item(item.get("index"),
                        item.get("name"),
                        item.get("eff"),
                        item.get("des"),
                        item.get("rare"),
                        item.get("exclusive"))
        if new_item.index not in global_var.items_list.keys():
            global_var.items_list[new_item.index] = new_item
            cnt += 1
        else:
            RLDebug.debug("无法载入序号为{}的藏品{}: 相同编号的藏品{}已存在".format(
                new_item.index,
                new_item.name,
                global_var.items_list[new_item.index].name
            ), type='error', who='Items')

    RLDebug.debug("藏品文件加载完成，共载入了{}个藏品".format(cnt), type='success', who='Items')
