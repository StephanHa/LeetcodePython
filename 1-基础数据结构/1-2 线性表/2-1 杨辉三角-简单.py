# 118 杨辉三角（简单）
# https://leetcode.cn/problems/pascals-triangle/
# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。每行第一个和最后一个都是1。

# 方法1，直接模拟
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = list()
        for i in range(numRows):
            row = list()
            for j in range(i+1):
                if j == 0 or j == i: # 首尾都为1
                    row.append(1)
                else: # 其它为上一行，当前j的前两个元素之和
                    row.append(result[i-1][j] + result[i-1][j-1])
            result.append(row)
        return result


numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


# 执行用时：40 ms, 在所有 Python3 提交中击败了39.38%的用户
# 内存消耗：14.8 MB, 在所有 Python3 提交中击败了94.44%的用户
# 通过测试用例：14 / 14
