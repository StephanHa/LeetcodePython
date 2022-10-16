# 给你两个按 非递减顺序 排列的整数数组nums1 和 nums2，另有两个整数 m 和 n ，
# 分别表示 nums1 和 nums2 中的元素数目。
# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
#
# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，
# nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
#
# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xnumcr/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# 方法1，借用额外数组nums存储nums1的元素，再将nums2和nums比较大小填写入nums1
# from typing import List
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         nums = nums1[:m]
#         i, j, x = 0, 0, 0
#         while i < m and j < n:
#             if nums[i] < nums2[j]:
#                 nums1[x] = nums[i]
#                 i += 1
#                 x += 1
#             else:
#                 nums1[x] = nums2[j]
#                 j += 1
#                 x += 1
#         if i < m:
#             nums1[x:] = nums[i:]
#         if j < n:
#             nums1[x:] = nums2[j:]
#         return nums1
#
#
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# # 输出：[1,2,2,3,5,6]
# # 解释：需要合并 [1,2,3] 和 [2,5,6] 。
#
# test = Solution()
# print(test.merge(nums1, m, nums2, n))

# 执行用时：40 ms, 在所有 Python3 提交中击败了45.35%的用户
# 内存消耗：15.1 MB, 在所有 Python3 提交中击败了7.89%的用户
# 通过测试用例：59 / 59


# 方法2，从后往前比较，大的填写到nums1后面
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, x = m-1, n-1, (m+n-1)
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[x] = nums1[i]
                i -= 1
            else:
                nums1[x] = nums2[j]
                j -= 1
            x -= 1
        while i >= 0:
            nums1[x] = nums1[i]
            x -= 1
            i -= 1
        while j >= 0:
            nums1[x] = nums2[j]
            x -= 1
            j -= 1
        return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
# 输出：[1,2,2,3,5,6]
# 解释：需要合并 [1,2,3] 和 [2,5,6] 。

test = Solution()
print(test.merge(nums1, m, nums2, n))


# 执行用时：32 ms, 在所有 Python3 提交中击败了90.89%的用户
# 内存消耗：15.1 MB, 在所有 Python3 提交中击败了11.04%的用户
# 通过测试用例：59 / 59

