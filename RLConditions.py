import RLDebug
import global_var


# 检定


def check_logic(condition: str) -> bool:
    # 基础比较语句的检定

    RLDebug.split(1)
    RLDebug.debug("开始判定语句【{}】".format(condition), who="Conditions")

    # 条件语句中的符号
    symbols = ['>', '<', '?', '!', '=']

    # 查找第一个符号
    index = float('inf')
    for symbol in symbols:
        first_occurrence = condition.find(symbol)
        if first_occurrence != -1 and first_occurrence < index:
            index = first_occurrence

    # 要比较的属性
    prop = condition[:index]

    # 要比较的属性的值
    val_compare = 0

    # 数值比较结果
    result = False

    # 拆分数组
    parse_value = []

    if condition[index + 1] == '=':
        # 比较式中的符号
        # 如果符号是'==', '>=' 或者 '<='
        symbol_compare = condition[index:index + 2]
        # 比较中提供的值
        val_given = condition[index + 2:]
    else:
        # 其他情况
        symbol_compare = condition[index:index + 1]
        val_given = condition[index + 1:]
        if val_given[0] == '[':
            # 如果提供的值是一个数组就拆分成列表
            parse_value = val_given[1:-1].split(',')

    if prop == 'item':
        RLDebug.debug("判断属性{}".format(prop), who="Conditions")
        RLDebug.debug("判断符号:{}".format(symbol_compare), who="Conditions")
        RLDebug.debug("提供值:{}".format(parse_value), who="Conditions")
        if symbol_compare == '?':
            # 如果有某物品返回真，没有返回假
            for item_index in parse_value:
                if item_index in global_var.player_info.attained_items:
                    RLDebug.debug("子表达式{}判定结束，结果为真".format(condition), who="Conditions")
                    RLDebug.split(1)
                    return True
            RLDebug.debug("子表达式判定结束，结果为假", who="Conditions")
            RLDebug.split(1)
            return False
        elif symbol_compare == '!':
            # 如果有某物品返回假，没有返回真
            for item_index in parse_value:
                if item_index in global_var.player_info.attained_items:
                    RLDebug.debug("子表达式判定结束，结果为假", who="Conditions")
                    RLDebug.split(1)
                    return False
            RLDebug.debug("子表达式判定结束，结果为真", who="Conditions")
            RLDebug.split(1)
            return True
    elif prop == 'event':
        RLDebug.debug("判断属性{}".format(prop), who="Conditions")
        RLDebug.debug("判断符号:{}".format(symbol_compare), who="Conditions")
        RLDebug.debug("提供值:{}".format(parse_value), who="Conditions")
        if symbol_compare == '?':
            # 如果有某物品返回真，没有返回假
            for item_index in parse_value:
                if item_index in global_var.player_info.experienced_events:
                    RLDebug.debug("子表达式判定结束，结果为真", who="Conditions")
                    RLDebug.split(1)
                    return True
            RLDebug.debug("子表达式判定结束，结果为假", who="Conditions")
            RLDebug.split(1)
            return False
        elif symbol_compare == '!':
            # 如果有某物品返回假，没有返回真
            for item_index in parse_value:
                if item_index in global_var.player_info.experienced_events:
                    RLDebug.debug("子表达式判定结束，结果为假", who="Conditions")
                    RLDebug.split(1)
                    return False
            RLDebug.debug("子表达式判定结束，结果为真", who="Conditions")
            RLDebug.split(1)
            return True
    else:
        if global_var.player_info.adjustments.get(prop):
            val_compare = global_var.player_info.adjustments.get(prop)
        val_given = int(val_given)
        if symbol_compare == '>':
            result = val_compare > val_given
        elif symbol_compare == '<':
            result = val_compare < val_given
        elif symbol_compare == '==':
            result = val_compare == val_given
        elif symbol_compare == '>=':
            result = val_compare >= val_given
        elif symbol_compare == '<=':
            result = val_compare <= val_given

    RLDebug.debug("判断属性{}(判断值:{})".format(prop, val_compare), who="Conditions")
    RLDebug.debug("判断符号:{}".format(symbol_compare), who="Conditions")
    RLDebug.debug("提供值:{}".format(val_given), who="Conditions")

    if result is True:
        RLDebug.debug("子表达式判定结束，结果为真", who="Conditions")
        RLDebug.split(1)
        return True
    else:
        RLDebug.debug("子表达式判定结束，结果为假", who="Conditions")
        RLDebug.split(1)
        return False


def parse_conditions(condition: str) -> (list, int):
    # 将符合条件语句拆分成基本条件语句
    # 拆分后的条件判断语句
    parsed_conditions = []
    # 总语句的长度
    length = len(condition)
    # 当前下标
    current = 0
    i = -1
    while i < length - 1:
        i = i + 1
        if condition[i] == '(':
            (sub_conditions, sub_length) = parse_conditions(condition[i + 1:])
            parsed_conditions.append(sub_conditions)
            i = i + sub_length + 1
            current = current + sub_length + 2
        elif condition[i] == '&':
            if condition[current:i] != "":
                parsed_conditions.append(condition[current:i])
            parsed_conditions.append('&')
            current = i + 1
        elif condition[i] == '|':
            if condition[current:i] != "":
                parsed_conditions.append(condition[current:i])
            parsed_conditions.append('|')
            current = i + 1
        elif condition[i] == ')':
            if condition[current:i] != "":
                parsed_conditions.append(condition[current:i])
            return parsed_conditions, i
        else:
            continue
    if condition[current:] != "":
        parsed_conditions.append(condition[current:])
    RLDebug.debug("已将表达式{}拆分为子表达式{}".format(condition, parsed_conditions), who="Conditions")
    return parsed_conditions, i


def test_parse(conditions: list, priority: int) -> None:
    # 输出拆分后条件语句的层级关系
    for condition in conditions:
        if type(condition) == str:
            RLDebug.debug('-' * 3 * priority + condition, who="Conditions")
        elif type(condition) == list:
            test_parse(condition, priority + 1)


def check(conditions: list) -> bool:
    if len(conditions) == 0:
        # 如果没有条件语句
        return True
    elif len(conditions) == 1:
        # 如果只有一个拆分后的条件语句或者一个列表
        return check(conditions[0]) if type(conditions[0]) == list else check_logic(conditions[0])
    else:
        # 若干个条件语句
        result = check(conditions[0]) if type(conditions[0]) == list else check_logic(conditions[0])
        for i in range(1, len(conditions), 2):
            if conditions[i] == '&':
                if result is True:
                    result = check(conditions[i + 1]) \
                        if type(conditions[i + 1]) == list \
                        else check_logic(conditions[i + 1])
                else:
                    return False
            elif conditions[i] == '|':
                if result is True:
                    return True
                else:
                    result = check(conditions[i + 1]) \
                        if type(conditions[i + 1]) == list \
                        else check_logic(conditions[i + 1])
            else:
                return False
    return result


def check_conditions(condition: str) -> bool:
    RLDebug.split(2)
    RLDebug.debug("开始判定条件表达式{}".format(condition), type='info', who="Conditions")
    if check(parse_conditions(condition)[0]):
        RLDebug.debug("判定完成，表达式{}的判定结果为真".format(condition), type='success', who="Conditions")
        RLDebug.split(2)
        return True
    else:
        RLDebug.debug("判定完成，表达式{}的判定结果为假".format(condition), type='success', who="Conditions")
        RLDebug.split(2)
        return False
