# 14. 最长公共前缀（简单）
# https://leetcode.cn/problems/longest-common-prefix/
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例：
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"

# 方法1，暴力破解（横向扫描）
# 思路：两两字符串从索引0开始比较，相同则index加1，不同则退出
# 终止条件：每次两个字符串比较结束，就判断公共前缀是否为空，为空则退出，不存在公共前缀
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]
        for i in range(1, len(strs)):
            index = 0
            length = min(len(result), len(strs[i]))
            # 两两字符串比较，从索引0开始，相同则加一，否则退出
            while index < length and result[index] == strs[i][index]:
                index += 1
            result = result[:index]
            # 如果为空，则不存在公共前缀，直接返回
            if not result:
                return result
        return result


# 示例1
strs = ["flower", "flow", "flight"]
# 输出："fl"
test = Solution()
print(test.longestCommonPrefix(strs))

# 执行用时：44 ms, 在所有 Python3 提交中击败了27.58%的用户
# 内存消耗：15.3 MB, 在所有 Python3 提交中击败了5.02%的用户
# 通过测试用例：124 / 124


# 方法2，纵向扫描
# 利用zip函数，将所有字符串按相同索引组成元素，判断转集合如果相同则长度为1
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        index = 0
        for item in zip(*strs):
            # 转集合去重判断长度
            if len(set(item)) == 1:
                index += 1
            else:
                break
        return strs[0][:index]


strs = ["flower", "flow", "flight"]
# 输出："fl"
test = Solution()
print(test.longestCommonPrefix(strs))

# 2022-08-27 11:52
# 执行用时：28 ms, 在所有 Python3 提交中击败了98.44%的用户
# 内存消耗：15.3 MB, 在所有 Python3 提交中击败了5.02%的用户
# 通过测试用例：124 / 124

# 2022-09-19 00:05
# 执行用时：40 ms, 在所有 Python3 提交中击败了56.62%的用户
# 内存消耗：15 MB, 在所有 Python3 提交中击败了75.38%的用户
# 通过测试用例：124 / 124
