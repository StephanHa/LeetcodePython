# 49 字母异位词分组
# https://leetcode.cn/problems/group-anagrams
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
# 字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。

# 示例：
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

# 输入: strs = [""]
# 输出: [[""]]

# 方法1，字典存储列表
# 关键点：异位字母词排序后都相同
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = dict()
        for item in strs:
            key = "".join(sorted(item))
            if key in result.keys():
                result[key].append(item)
            else:
                result[key] = list()
                result[key].append(item)
        return list(result.values())

strs = ["a"]
test49 = Solution()
print(test49.groupAnagrams(strs))

# 执行用时：48 ms, 在所有 Python3 提交中击败了86.66%的用户
# 内存消耗：18.2 MB, 在所有 Python3 提交中击败了40.46%的用户
# 通过测试用例：117 / 117


