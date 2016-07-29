#coding:utf8

import random

def randomname(length):
    if length <= 0 or not isinstance(length, int):
        return None
    name = ''
    for x in xrange(0, length):
        temp = random.choice('zxcvbnmasdfghjklqwertyuiop')
        name += temp
    return name