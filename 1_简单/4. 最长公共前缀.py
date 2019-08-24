# -*- coding:utf-8 -*- 

# Copyright 2019-08-24 BWP 
# Created by yaoyao <mryao.com@gmail.com> at '2019-08-24 15:55'

# 最长前缀

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return "不存在"
        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]

        return s1

if __name__ == '__main__':
    a = Solution()
    strs = ["flower","flow","flight"]
    a.longestCommonPrefix(strs)