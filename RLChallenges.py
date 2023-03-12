import RLConditions
import RLDebug
import global_var
from RLCollections import Collections


class Challenges(Collections):
    # 挑战类
    def __init__(self, index: int, name: str, des: str, req: str, gen: str, suc: str, fai: str):
        super(Challenges, self).__init__(index, name, "", des, False)

        # 需求语句，满足需求即可获得额外信息或是修正
        self.requirements = req

        # 通用信息，无论是否检定成功
        self.general_info = gen

        # 检定成功信息
        self.success_info = suc

        # 检定失败信息
        self.fail_info = fai

        # 额外修正
        self.adjustments = {}

    def challenge_check(self) -> bool:
        # 挑战检定
        if RLConditions.check_conditions(self.requirements):
            for adjustment in self.adjustments.keys():
                global_var.player_info.add_adjustment(adjustment, self.adjustments[adjustment])
            RLDebug.debug("挑战{}检定成功，获得了增益并且解锁了额外信息".format(self.name), type='info', who='Challenges')
            return True
        else:
            RLDebug.debug("挑战{}检定失败".format(self.name), type='info', who='Challenges')
            return False

    def add_adjustment(self, adjustment, val):
        self.adjustments[adjustment] = val
            
            
def load_challenges(challenge_file):
    # 应用挑战文件
    cnt = 0

    # 检测挑战文件是否启用
    if not challenge_file.get('enabled') is True:
        RLDebug.debug("挑战文件未被启用或格式错误，跳过本次解析", type='error', who='Challenges')
        return

    # 检测配置文件版本是否符合
    if not challenge_file.get('version') in [global_var.current_version, '*', 'all']:
        RLDebug.debug(
            "挑战文件版本不符或格式错误，跳过本次解析<br>当前版本: {}<br>配置文件版本: {}".format(
                global_var.current_version,
                challenge_file.get('version')),
            type='error', who='Challenges')
        return

    # 遍历挑战
    for challenge in challenge_file.get('challenges'):
        required_keys = ['index', 'name', 'des', 'req', 'gen', 'suc', 'fai']
        missed_keys = []
        for key in required_keys:
            if key not in challenge.keys():
                missed_keys.append(key)
        # 如果有缺失的关键键值对
        if not len(missed_keys) == 0:
            RLDebug.debug("已损坏的数据文件：{0}, 缺失如下键值对:{1}, 跳过当前数据文件".format(
                challenge_file.get('name'), missed_keys),
                type='error', who='Challenges')
            return
        new_challenge = Challenges(challenge.get("index"),
                                   challenge.get("name"),
                                   challenge.get("des"),
                                   challenge.get("req"),
                                   challenge.get("gen"),
                                   challenge.get("suc"),
                                   challenge.get("fai"))
        if 'adj' in challenge.keys():
            for adjustment in challenge.get('adj'):
                new_challenge.add_adjustment(adjustment, challenge.get('adj')[adjustment])
        if new_challenge.index not in global_var.challenges_list.keys():
            global_var.challenges_list[new_challenge.index] = new_challenge
            cnt += 1
            RLDebug.debug("载入了序号为{}的挑战{}".format(
                new_challenge.index,
                new_challenge.name),
                type='success', who='Challenges')
        else:
            RLDebug.debug("无法载入序号为{}的挑战{}: 相同编号的挑战{}已存在".format(
                new_challenge.index,
                new_challenge.name,
                global_var.challenges_list[new_challenge.index].name
            ), type='error', who='Challenges')

    RLDebug.debug("挑战文件加载完成，共载入了{}个挑战".format(cnt), type='success', who='Challenges')
