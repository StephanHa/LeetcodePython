# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 说明：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/x21ib6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 方法1，排序+两两比较
# 跳过两两相等的，当出现不相等，则返回
# from typing import List
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         nums = sorted(nums)
#         n = len(nums)
#         i = 0
#         while i < n:
#             if i == (n - 1):
#                 return nums[i]
#             if nums[i] == nums[i + 1]:
#                 i += 2
#             else:
#                 return nums[i]
#
# nums = [2,2,3,4,6,4,6]
# # 输出: 3
# test = Solution()
# print(test.singleNumber(nums))


# 执行用时：52 ms, 在所有 Python3 提交中击败了34.38%的用户
# 内存消耗：16.7 MB, 在所有 Python3 提交中击败了94.58%的用户
# 通过测试用例：61 / 61


# 方法2，异或运算
# 任何数和自己做异或运算，结果为 0; a^a=0
# 任何数和 0 做异或运算，结果还是自己; a^0 = a
# 异或运算中，满足交换律和结合律，也就是a^b^a = b^a^a = b^(a^a) = b^0 = b
# 作者：果冻
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/x21ib6/?discussion=dBVMYV
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


nums = [2,2,3,4,6,4,6]
# 输出: 3
test = Solution()
print(test.singleNumber(nums))
