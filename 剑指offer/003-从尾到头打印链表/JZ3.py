# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        res = []                            # create an empty list
        while listNode:                     # while element in ListNode
            res.append(listNode.val)        # put the value in the list one by one
            listNode = listNode.next        # to next value
        return res[::-1]                    # reverse the list [::-1] for the output