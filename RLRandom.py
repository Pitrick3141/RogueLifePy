import math
import random

import RLDebug


class WeightedRandom:
    def __init__(self) -> None:
        self.prepared_weight_list = {}
        self.index_list = []

    def random_initialize(self, weight_list: dict) -> None:
        list1 = []
        list2 = []
        for k, v in weight_list.items():
            if v != 0:
                list1.append(k)
                list2.append(v)
        weight_list = dict(zip(list1, list2))
        weight_sum = 0
        length = len(weight_list)
        small_average = []
        big_average = []
        for i in weight_list:
            weight_sum += weight_list[i]
        average_weight = 1.0 * weight_sum / length
        for item in weight_list:
            if weight_list[item] > average_weight:
                big_average.append((weight_list[item], item))
            else:
                small_average.append((weight_list[item], item))
            self.index_list.append(item)
        for i in range(length):
            if len(small_average) > 0:
                if len(big_average) > 0:
                    self.prepared_weight_list[small_average[0][1]] = \
                        (small_average[0][0] / average_weight, big_average[0][1])
                    big_average[0] = (big_average[0][0] - average_weight + small_average[0][0], big_average[0][1])
                    if average_weight - big_average[0][0] > 0.00000001:
                        small_average.append((big_average[0]))
                        del big_average[0]
                else:
                    self.prepared_weight_list[small_average[0][1]] = \
                        (small_average[0][0] / average_weight, small_average[0][1])
                del small_average[0]
            else:
                self.prepared_weight_list[big_average[0][1]] = (big_average[0][0] / average_weight, big_average[0][1])
                del big_average[0]
        RLDebug.debug("已初始化包含{}个对象的随机数生成器".format(length), type='success', who=self.__class__.__name__)

    def get_random_index(self) -> int:
        length = len(self.prepared_weight_list)
        random_number = random.random() * length
        int_random = int(math.floor(random_number))
        current = self.prepared_weight_list.get(self.index_list[int_random])
        if current[0] > random_number - int_random:
            ret = self.index_list[int_random]
        else:
            ret = current[1]
        RLDebug.debug("随机数:{}({}) 当前权重比{} 返回结果:{}".format(
            random_number, int_random, current[0], ret), who=self.__class__.__name__)
        return ret
