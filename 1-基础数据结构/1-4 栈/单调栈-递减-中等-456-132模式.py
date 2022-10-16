# 456. 132 模式（中等）（好难理解）
# 给你一个整数数组 nums ，数组中共有 n 个整数。132 模式的子序列
# 由三个整数 nums[i]、nums[j] 和 nums[k] 组成，并同时满足：i < j < k 和 nums[i] < nums[k] < nums[j] 。
# 如果 nums 中存在 132 模式的子序列 ，返回 true ；否则，返回 false 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/132-pattern
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#
# 示例1
# 输入：nums = [1,2,3,4]
# 输出：false
# 解释：序列中不存在 132 模式的子序列。

# 示例2
# 输入：nums = [3,1,4,2]
# 输出：true
# 解释：序列中有 1 个 132 模式的子序列： [1, 4, 2]

# 部分用例失败
# from typing import List
# class Solution:
#     def find132pattern(self, nums: List[int]) -> bool:
#         stack = list()
#         for num in nums:
#             flag = False
#             while stack and stack[-1] > num:
#                 stack.pop()
#                 flag = True
#             if stack and flag:
#                 return True
#             stack.append(num)
#         return False
#
# # nums = [3,1,4,2] True
# # nums = [1,2,3,4] False
# nums = [3,5,0,3,4] # 运行失败
# test = Solution()
# print(test.find132pattern(nums))


# 方法1，枚举+单调栈
# 参考：方法二：枚举 1 https://leetcode.cn/problems/132-pattern/solution/132mo-shi-by-leetcode-solution-ye89/


