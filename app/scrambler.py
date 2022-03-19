""" 魔方打乱生成 """

import random


def scrambler():
    return [random.randint(0, 1) for _ in range(0, 5)]