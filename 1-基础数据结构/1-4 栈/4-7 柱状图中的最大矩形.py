# 84. 柱状图中最大的矩形（困难）
# https://leetcode.cn/problems/largest-rectangle-in-histogram/
#
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。

# 示例：
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10

# 输入： heights = [2,4]
# 输出： 4

# 方法1，暴力方法
# https://leetcode.cn/problems/largest-rectangle-in-histogram/solution/dong-hua-yan-shi-dan-diao-zhan-84zhu-zhu-03w3/
# 时间复杂度：O(n*n)
# 空间复杂度：O(n)
# 基本思路是，对于当前考察的矩形，分别向左和向右扩展其边界，直到边界索引对应的矩形高度，小于当前考察的矩形的高度。
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        lenght = len(heights)
        for i in range(lenght):
            currtent_height = heights[i]
            left_index, right_index = i, i
            # 寻找当前高度的左边界
            while (i-1)>=0 and heights[i-1] >= currtent_height:
                left_index -= 1
            # 寻找当前高度的右边界
            while (i+1) < lenght and heights[i+1] >= currtent_height:
                right_index += 1
            # 计算当前高度的最大矩形
            result = max(result, (right_index - left_index + 1)*currtent_height)
        return result

# 方法2，单调栈（递增）
from typing import List
class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1] # 柱子的索引，栈低用-1表示
        result = 0
        for i in range(len(heights)):
            while len(stack) > 1 and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                result = max(result, heights[index] * (i - stack[-1] - 1))
            stack.append(i)
        for i in range(len(stack)-1):
            index = stack.pop()
            result = max(result, heights[index] * (len(heights)-1 - stack[-1]))
        return result

# 执行用时：308 ms, 在所有 Python3 提交中击败了59.36%的用户
# 内存消耗：26.2 MB, 在所有 Python3 提交中击败了58.34%的用户
# 通过测试用例：98 / 98

