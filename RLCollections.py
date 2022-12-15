class Collections:
    # 可收集物品类
    def __init__(self, index, name, des, eff, exclusive):
        self.index = index
        self.name = name
        self.des = des
        self.eff = eff
        self.exclusive = exclusive
        self.exclude = []
        self.require = []
