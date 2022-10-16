# 给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。

# 方法1，哈希表记录字符数量
class Solution:
    def firstUniqChar(self, s: str) -> int:
        result = dict()
        n = len(s)
        # 哈希表统计所有字符的数量
        for i in range(n):
            if s[i] in result.keys():
                result[s[i]][0] += 1  # count += 1
            else:
                result[s[i]] = [1, i] # [count, index]
        for item in s:
            # 返回第一个数量为1的字符的索引
            if result[item][0] == 1:
                return result[item][1]
        # 如果不存在，则返回-1
        return -1


s = "loveleetcode"
# 输出: 2
test = Solution()
print(test.firstUniqChar(s))

# 执行用时：168 ms, 在所有 Python3 提交中击败了20.80%的用户
# 内存消耗：15.1 MB, 在所有 Python3 提交中击败了69.01%的用户
# 通过测试用例：105 / 105

