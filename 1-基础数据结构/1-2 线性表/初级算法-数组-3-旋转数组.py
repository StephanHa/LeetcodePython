# 给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右轮转 1 步: [7,1,2,3,4,5,6]
# 向右轮转 2 步: [6,7,1,2,3,4,5]
# 向右轮转 3 步: [5,6,7,1,2,3,4]
#
# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/x2skh7/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 方法1，旋转再旋转 空间复杂度O(1)
# from typing import List
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         k = k % n  # k会大于n，因此需取模
#         if k == 0:
#             return
#         # 前n - k段首尾两两调换
#         n_end = n - k - 1
#         for n_start in range((n - k) // 2):
#             nums[n_start], nums[n_end] = nums[n_end], nums[n_start]
#             n_end -= 1
#         # 后k段首尾两两调换
#         k_end = n - 1
#         for k_start in range(n-k, (n - k + k // 2)):
#             nums[k_start], nums[k_end] = nums[k_end], nums[k_start]
#             k_end -= 1
#         # 全部首尾两两调换
#         end = n - 1
#         for start in range(0, n // 2):
#             nums[start], nums[end] = nums[end], nums[start]
#             end -= 1
#         return nums
#
#
# nums = [1,2,3,4,5,6,7]
# k = 3
# # 输出: [5,6,7,1,2,3,4]
# test = Solution()
# print(test.rotate(nums, k))

# 执行用时：48 ms, 在所有 Python3 提交中击败了65.50%的用户
# 内存消耗：21.3 MB, 在所有 Python3 提交中击败了15.88%的用户
# 通过测试用例：38 / 38


# 方法2，借用临时数组，空间复杂度O(n)
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        temp = [0 for _ in range(n)]
        for i in range(n):
            temp[(i+k)%n] = nums[i]
        return temp

nums = [1,2,3,4,5,6,7]
k = 3
# 输出: [5,6,7,1,2,3,4]
test = Solution()
print(test.rotate(nums, k))
