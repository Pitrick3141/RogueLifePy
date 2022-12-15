from RLCollections import Collections


class Item(Collections):
    # 藏品类
    def __init__(self, index: int, name: str, eff: str, des: str, rare: int, exclusive=False):
        super(Item, self).__init__(index, name, eff, des, exclusive)
        self.rare = rare
        self.adjustments = {}

    def addAdjustment(self, adjustment: str, value: int):
        if adjustment not in self.adjustments.keys():
            self.adjustments[adjustment] = value
        return
