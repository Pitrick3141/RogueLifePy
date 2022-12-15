import global_var
import RLDebug


# 玩家信息
class Player:
    def __init__(self):
        self.adjustments = {}
        self.attained_items = []

    def addAdjustment(self, adjustment: str, value: int) -> None:
        if adjustment not in self.adjustments.keys():
            self.adjustments[adjustment] = value
            RLDebug.debug("获得了修正【{}】,修正值为{}".format(adjustment, value),
                          type='success', who=self.__class__.__name__)
        else:
            self.adjustments[adjustment] += value
            RLDebug.debug("修正【{}】获得了变化{},新的修正值为{}".format(adjustment, value, self.adjustments[adjustment]),
                          type='success', who=self.__class__.__name__)

        return

    def attainItem(self, index: int) -> bool:
        if index in global_var.items_list.keys():
            item = global_var.items_list.get(index)
            for excluded in item.exclude:
                if excluded in self.attained_items:
                    RLDebug.debug("无法获取序号为{}的藏品【{}】: 与序号为{}的藏品【{}】互斥".format(index, item.name, excluded.index, excluded.name),
                                  type='error', who=self.__class__.__name__)
                    return False
            for required in item.require:
                if required not in self.attained_items:
                    RLDebug.debug("无法获取序号为{}的藏品【{}】: 需要先获取序号为{}的藏品【{}】".format(index, item.name, required.index, required.name),
                                  type='error', who=self.__class__.__name__)
            RLDebug.debug("获取了序号为{}的藏品【{}】".format(index, item.name),
                          type='success', who=self.__class__.__name__)
            for adjustment in item.adjustments:
                self.addAdjustment(adjustment, item.adjustments[adjustment])
            self.attained_items.append(item)
            return True
        else:
            RLDebug.debug("无法获取序号为{}的藏品: 不存在该物品".format(index), type='error', who=self.__class__.__name__)

    def printPlayerInfo(self):
        RLDebug.split()
        RLDebug.debug("玩家信息", who=self.__class__.__name__)
        RLDebug.debug("修正列表:", who=self.__class__.__name__)
        RLDebug.split(1)
        for adjustment in self.adjustments:
            RLDebug.debug("修正【{}】值为{}".format(adjustment, self.adjustments[adjustment]), who=self.__class__.__name__)
        RLDebug.debug("获得的藏品列表:", who=self.__class__.__name__)
        RLDebug.split(1)
        for item in self.attained_items:
            RLDebug.debug("序号为{}的藏品【{}】".format(item.index, item.name), who=self.__class__.__name__)
        RLDebug.split()


def init():
    global_var.player_info = Player()


def load_player_info(data_file):
    # 读取玩家信息存档

    # 检测玩家信息存档版本是否符合
    if not data_file.get('version') in [global_var.current_version, '*', 'all']:
        RLDebug.debug(
            "玩家信息存档版本不符或格式错误，跳过本次解析<br>当前版本: {}<br>玩家信息存档版本: {}".format(
                global_var.current_version,
                data_file.get('version')),
            type='error', who='Player')
        return

    player_load = data_file.get('player')

    required_keys = ['adjustments', 'attained_items']
    missed_keys = []
    for key in required_keys:
        if key not in player_load.keys():
            missed_keys.append(key)
    # 如果有缺失的关键键值对
    if not len(missed_keys) == 0:
        RLDebug.debug("已损坏的数据文件：{0}, 缺失如下键值对:{1}, 跳过当前数据文件".format(
            data_file.get('name'), missed_keys),
            type='error', who='Player')
        return

    global_var.player_info.adjustments = player_load.get('adjustments')
    global_var.player_info.attained_items = player_load.get('attained_items')
    global_var.save_name = data_file.get('name')

    RLDebug.debug("玩家信息存档{}读取完成，共载入了{}个藏品，{}条修正".format(
        data_file.get('name'),
        len(player_load.get('attained_items')),
        len(player_load.get('attained_items'))),
        type='success', who='Player')
