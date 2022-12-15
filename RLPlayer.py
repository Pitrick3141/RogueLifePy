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
            RLDebug.debug("获得了修正{},修正值为{}".format(adjustment, value),
                          type='success', who=self.__class__.__name__)
        else:
            self.adjustments[adjustment] += value
            RLDebug.debug("修正{}获得了变化{},新的修正值为{}".format(adjustment, value, self.adjustments[adjustment]),
                          type='success', who=self.__class__.__name__)

        return

    def attainItem(self, index: int) -> bool:
        if index in global_var.items_list.keys():
            item = global_var.items_list.get(index)
            for excluded in item.exclude:
                if excluded in self.attained_items:
                    RLDebug.debug("无法获取序号为{}的藏品{}: 与序号为{}的藏品{}互斥".format(index, item.name, excluded.index, excluded.name),
                                  type='error', who=self.__class__.__name__)
                    return False
            for required in item.require:
                if required not in self.attained_items:
                    RLDebug.debug("无法获取序号为{}的藏品{}: 需要先获取序号为{}的藏品{}".format(index, item.name, required.index, required.name),
                                  type='error', who=self.__class__.__name__)
            RLDebug.debug("获取了序号为{}的藏品{}".format(index, item.name),
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
        for adjustment in self.adjustments:
            RLDebug.debug("{}的修正值为{}".format(adjustment, self.adjustments[adjustment]), who=self.__class__.__name__)
        RLDebug.debug("获得的藏品列表:", who=self.__class__.__name__)
        for item in self.attained_items:
            RLDebug.debug("序号为{}的藏品{}".format(item.index, item.name), who=self.__class__.__name__)
        RLDebug.split()


def init():
    global_var.player_info = Player()
