# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        for line in array:
            if target in line:
                return True
                break
        return False