# -*- coding:utf-8 -*- 

# Copyright 2019-07-26 BWP 
# Created by yaoyao <mryao.com@gmail.com> at '2019-07-26 21:46'


class Node(object):
    """
    data: 节点保存的数据
    next 保存下一个节点对象
    """

    def __init__(self,data,pnext=None):
        self.data = data
        self._next = pnext

    def __repr__(self):
        """
        用来定义Node的字符输出
        :return:
        """
        return str(self.data)

    def append(self,dataOrNode):
        item = None

        if isinstance(dataOrNode,Node):
            item = dataOrNode
