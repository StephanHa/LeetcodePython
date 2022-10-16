# 11. 盛最多水的容器（中等）
# https://leetcode.cn/problems/container-with-most-water/
# 给定一个长度为n的整数数组height。有n条垂线，第i条线的两个端点是 (i, 0) 和 (i, height[i]) 。
# 找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。返回容器可以储存的最大水量。
# 说明：你不能倾斜容器。
#
height = [1,8,6,2,5,4,8,3,7]
# 输出：49
# 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为49。
#
# 关键：1、相同情况下两边距离越远越好；2、区域受限于较短边。

# 方法1，暴力破解
from typing import List
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         n = len(height)
#         result = 0
#         for i in range(n):
#             for j in range(i, n):
#                 temp = (j - i) * min(height[i], height[j])
#                 result = max(result, temp)
#         return result

# 执行结果：超出时间限制


# 方法2，双指针
# 时间复杂度：O(n) 双指针最多遍历整个数组一次
# 空间复杂度：O(1) 只需额外常数级别的空间

class Solution:
    def maxArea(self, height:List[int]) -> int:
        left, right = 0, len(height)-1
        result = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            result = max(result, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return result


# 执行用时：232 ms, 在所有 Python3 提交中击败了36.83%的用户
# 内存消耗：25.3 MB, 在所有 Python3 提交中击败了65.95%的用户
# 通过测试用例：60 / 60

test = Solution()
print(test.maxArea(height))
