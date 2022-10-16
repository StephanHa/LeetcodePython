# 42 接雨水
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
# 示例：
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
#
# 输入：height = [4,2,0,3,2,5]
# 输出：9


# 方法1，单调递减栈
# 单调栈存储的是柱子的序号
# 1、当前柱子高度比栈顶对应的高度低，则加入栈；
# 2、当前柱子高度比栈顶对应的高度高，则说明会形成低洼位置，可以接雨水。
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = list() # 柱子数组的序号
        result = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                temp = stack.pop()
                # 如果栈为空，则说明左边没有更高柱子，无法接雨水
                if not stack: break
                # 如果栈非空，则说明左边有更高的柱子
                h = min(height[i], height[stack[-1]]) - height[temp]
                w = i - stack[-1] - 1
                result += h * w
            stack.append(i)
        return result

# 执行用时：60 ms, 在所有 Python3 提交中击败了66.86%的用户
# 内存消耗：16.4 MB, 在所有 Python3 提交中击败了63.13%的用户
# 通过测试用例：322 / 322

