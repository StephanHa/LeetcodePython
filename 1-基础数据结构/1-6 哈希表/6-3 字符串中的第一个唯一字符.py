# 387. 字符串中的第一个唯一字符
# https://leetcode.cn/problems/first-unique-character-in-a-string/
# 给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。
#
# 方法1，哈希表存储频数
# 先统计字符数量，再按字符串顺序找到第一个数量为1的字符，并返回其索引
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_count = dict()
        for key in s:
            if key in dict_count.keys():
                dict_count[key] += 1
            else:
                dict_count[key] = 1
        for index, value in enumerate(s):
            if dict_count[value] == 1:
                return index
        return -1

# 执行用时：132 ms, 在所有 Python3 提交中击败了33.05%的用户
# 内存消耗：15.2 MB, 在所有 Python3 提交中击败了17.02%的用户
# 通过测试用例：105 / 105


# 方法2，哈希表存储索引
# https://leetcode.cn/problems/first-unique-character-in-a-string/solution/zi-fu-chuan-zhong-de-di-yi-ge-wei-yi-zi-x9rok/
# 只出现一次的字符，值为其索引，如果出现两次以上，值则设置为-1，循环找出最小索引，否则返回-1
class Solution2:
    def firstUniqChar(self, s: str) -> int:
        temp_dict = dict()
        for index, value in enumerate(s):
            if value in temp_dict.keys():
                temp_dict[value] = -1
            else:
                temp_dict[value] = index
        first = len(s)
        for pos in temp_dict.values():
            if pos != -1 and pos < first:
                first = pos
        if first == len(s):
            first = -1
        return first

# 执行用时：152 ms, 在所有 Python3 提交中击败了25.29%的用户
# 内存消耗：15 MB, 在所有 Python3 提交中击败了94.27%的用户
# 通过测试用例：105 / 105

