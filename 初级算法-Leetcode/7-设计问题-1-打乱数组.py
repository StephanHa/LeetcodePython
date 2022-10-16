# 给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。打乱后，数组的所有排列应该是等可能的。
#
# 实现 Solution class:
# Solution(int[] nums) 使用整数数组 nums 初始化对象
# int[] reset() 重设数组到它的初始状态并返回
# int[] shuffle() 返回数组随机打乱后的结果
#
# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xn6gq1/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# 方法1，直接调用random函数
# import random
# from typing import List
# class Solution:
#     def __init__(self, nums: List[int]):
#         self.nums = nums
#
#     def reset(self) -> List[int]:
#         return self.nums
#
#     def shuffle(self) -> List[int]:
#         temp = self.nums[:]
#         random.shuffle(temp)
#         return temp
#
#
# # Solution solution = new Solution([1, 2, 3]);
# # solution.shuffle();    // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。例如，返回 [3, 1, 2]
# # solution.reset();      // 重设数组到它的初始状态 [1, 2, 3] 。返回 [1, 2, 3]
# # solution.shuffle();    // 随机返回数组 [1, 2, 3] 打乱后的结果。例如，返回 [1, 3, 2]
#
# nums = [1, 2, 3]
# solution = Solution(nums)
# print(solution.shuffle())
# print(solution.reset())
# print(solution.shuffle())

# 执行用时：100 ms, 在所有 Python3 提交中击败了93.78%的用户
# 内存消耗：18.8 MB, 在所有 Python3 提交中击败了30.04%的用户
# 通过测试用例：8 / 8



# 方法2，随机获取一个元素与第一个元素交换
import random
from typing import List
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = self.nums.copy()

    def reset(self) -> List[int]:
        self.nums = self.original.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        n = len(self.nums)
        for i in range(n):
            j = random.randrange(i, n)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


nums = [1, 2, 3]
solution = Solution(nums)
print(solution.shuffle())
print(solution.reset())
print(solution.shuffle())

# 执行用时：112 ms, 在所有 Python3 提交中击败了76.82%的用户
# 内存消耗：18.9 MB, 在所有 Python3 提交中击败了16.54%的用户
# 通过测试用例：8 / 8
