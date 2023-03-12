import RLDebug
import RLRandom
from RLCollections import Collections
import global_var


class Events(Collections):
    # 事件类
    def __init__(self, index: int, name: str, rare: int, des: str, actions: list, exclusive=False):
        super(Events, self).__init__(index, name, des, "", exclusive)
        # 稀有度
        self.rare = rare

        # 挑战列表，通过检定可获得更多信息
        self.challenges = []

        # 藏品列表，经历事件可获得如下的藏品
        self.items = []

        # 选择分支列表，通过选择及检定走向不同结果
        self.actions = actions

        # 互斥事件，有以下的事件则不会发生
        self.exclude = []

        # 需求事件，必须发生过以下的事件才会发生
        self.require = []

    def add_challenge(self, challenge):
        self.challenges.append(challenge)

    def add_item(self, item):
        self.items.append(item)


def load_events(event_file):
    # 应用事件文件
    cnt = 0

    # 检测事件文件是否启用
    if not event_file.get('enabled') is True:
        RLDebug.debug("事件文件未被启用或格式错误，跳过本次解析", type='error', who='Events')
        return

    # 检测配置文件版本是否符合
    if not event_file.get('version') in [global_var.current_version, '*', 'all']:
        RLDebug.debug(
            "事件文件版本不符或格式错误，跳过本次解析<br>当前版本: {}<br>配置文件版本: {}".format(
                global_var.current_version,
                event_file.get('version')),
            type='error', who='Events')
        return

    # 遍历事件
    for event in event_file.get('events'):
        required_keys = ['index', 'name', 'rare', 'des', 'actions', 'exclusive']
        missed_keys = []
        for key in required_keys:
            if key not in event.keys():
                missed_keys.append(key)
        # 如果有缺失的关键键值对
        if not len(missed_keys) == 0:
            RLDebug.debug("已损坏的数据文件：{0}, 缺失如下键值对:{1}, 跳过当前数据文件".format(
                event_file.get('name'), missed_keys),
                type='error', who='Events')
            return
        new_event = Events(event.get("index"),
                           event.get("name"),
                           event.get("rare"),
                           event.get("des"),
                           event.get("actions"),
                           event.get("exclusive"))
        if event.get("challenges"):
            challenges = event.get("challenges")
            for challenge in challenges:
                new_event.add_challenge(challenge)
        if event.get("items"):
            items = event.get("items")
            for item in items:
                new_event.add_item(item)
        if event.get("exclude"):
            new_event.exclude = event.get("exclude")
        if event.get("require"):
            new_event.require = event.get("require")
        if new_event.index not in global_var.events_list.keys():
            global_var.events_list[new_event.index] = new_event
            if not new_event.exclusive:
                global_var.events_weight_list[new_event.index] = new_event.rare
            cnt += 1
            RLDebug.debug("载入了序号为{}的事件{}【出现概率{}】".format(
                new_event.index,
                new_event.name,
                new_event.rare),
                type='success', who='Events')
        else:
            RLDebug.debug("无法载入序号为{}的事件{}: 相同编号的事件{}已存在".format(
                new_event.index,
                new_event.name,
                global_var.events_list[new_event.index].name
            ), type='error', who='Events')

    RLDebug.debug("事件文件加载完成，共载入了{}个事件".format(cnt), type='success', who='Events')
    initialize_random_event()


def initialize_random_event():
    global_var.random_events = RLRandom.WeightedRandom()
    global_var.random_events.random_initialize(global_var.events_weight_list)
    RLDebug.debug("事件随机器初始化完毕", type='success', who='Events')
