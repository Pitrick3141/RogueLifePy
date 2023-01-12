import RLDebug
import global_var
from RLCollections import Collections


class Actions(Collections):
    def __init__(self, index: int, name: str, des: str, req: int, adj: dict, suc: int, fai: int):
        super(Actions, self).__init__(index, name, des, "", False)

        # 成功需要的点数
        self.required_points = req

        # 可使用的修正及其系数
        self.available_adj = adj

        # 当前点数
        self.current_points = 0

        # 成功后的事件序号
        self.success_event = suc

        # 失败后的事件序号
        self.fail_event = fai

    def get_current_points(self):
        # 根据当前人物信息计算已有点数
        for adjustment in self.available_adj.keys():
            if adjustment in global_var.player_info.adjustments.keys():
                # 当前人物的修正值乘上该行动中修正的权重系数
                self.current_points += global_var.player_info.adjustments[adjustment] * self.available_adj[adjustment]


def load_actions(action_file):
    # 应用行动文件
    cnt = 0

    # 检测行动文件是否启用
    if not action_file.get('enabled') is True:
        RLDebug.debug("行动文件未被启用或格式错误，跳过本次解析", type='error', who='Actions')
        return

    # 检测配置文件版本是否符合
    if not action_file.get('version') in [global_var.current_version, '*', 'all']:
        RLDebug.debug(
            "行动文件版本不符或格式错误，跳过本次解析<br>当前版本: {}<br>配置文件版本: {}".format(
                global_var.current_version,
                action_file.get('version')),
            type='error', who='Actions')
        return

    # 遍历行动
    for action in action_file.get('actions'):
        required_keys = ['index', 'name', 'des', 'req', 'adj', 'suc', 'fai']
        missed_keys = []
        for key in required_keys:
            if key not in action.keys():
                missed_keys.append(key)
        # 如果有缺失的关键键值对
        if not len(missed_keys) == 0:
            RLDebug.debug("已损坏的数据文件：{0}, 缺失如下键值对:{1}, 跳过当前数据文件".format(
                action_file.get("name"), missed_keys),
                type='error', who='Actions')
            return
        new_action = Actions(action.get("index"),
                             action.get("name"),
                             action.get("des"),
                             action.get("req"),
                             action.get("adj"),
                             action.get("suc"),
                             action.get("fai"))
        if new_action.index not in global_var.actions_list.keys():
            global_var.actions_list[new_action.index] = new_action
            cnt += 1
            RLDebug.debug("载入了序号为{}的行动{}".format(
                new_action.index,
                new_action.name),
                type='success', who='Actions')
        else:
            RLDebug.debug("无法载入序号为{}的行动{}: 相同编号的行动{}已存在".format(
                new_action.index,
                new_action.name,
                global_var.actions_list[new_action.index].name
            ), type='error', who='Actions')

    RLDebug.debug("行动文件加载完成，共载入了{}个行动".format(cnt), type='success', who='Actions')
