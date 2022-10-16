# 503. 下一个更大元素 II（中等）
# 给定一个循环数组nums（nums[nums.length - 1]的下一个元素是nums[0]），返回nums中每个元素的 下一个更大元素 。
# 数字 x的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。
# 如果不存在，则输出 -1。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/next-greater-element-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 示例1
# 输入: nums = [1,2,1]
# 输出: [2,-1,2]
# 解释: 第一个 1 的下一个更大的数是 2；
# 数字 2 找不到下一个更大的数；
# 第二个 1 的下一个最大的数需要循环搜索，结果也是 2。

# 示例2
# 输入: nums = [1,2,3,4,3]
# 输出: [2,3,4,-1,4]

# 方法1，单调递减栈，两次遍历
# 单调栈元素为(num, index)
# 第一次遍历，入栈的代表未找到，出栈则代表已找到
# 第二次遍历，将栈内的再比较一次，还是剩余则表示不存在下个更大元素
from typing import List
# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         stack = list()  # (num, index)
#         length = len(nums)
#         result = [-1 for _ in range(length)]  # 初始值为-1，默认不存在
#         for i in range(length):
#             while stack and stack[-1][0] < nums[i]:
#                 result[stack.pop()[1]] = nums[i]
#             stack.append((nums[i], i))
#         for j in range(length):
#             if not stack:
#                 break
#             while stack and stack[-1][0] < nums[j]:
#                 result[stack.pop()[1]] = nums[j]
#         return result

# 执行用时：60 ms, 在所有 Python3 提交中击败了99.48%的用户
# 内存消耗：17.1 MB, 在所有 Python3 提交中击败了6.79%的用户
# 通过测试用例：223 / 223


# 方法2，单调栈+循环数组
# https://leetcode.cn/problems/next-greater-element-ii/solution/xia-yi-ge-geng-da-yuan-su-ii-by-leetcode-bwam/
# 栈元素为数组元素的下标
# 循环两次数组，转换成索引增加一倍，下标通过取模获取数组元素
from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [ -1 for _ in range(n) ]
        stack = list()  # 数组的元素下标
        for i in range(2 * n - 1):
            while stack and nums[stack[-1]] < nums[i % n]:
                result[stack.pop()] = nums[i % n]
            stack.append(i % n)
        return result

# 执行用时：108 ms, 在所有 Python3 提交中击败了32.63%的用户
# 内存消耗：16.5 MB, 在所有 Python3 提交中击败了39.13%的用户
# 通过测试用例：223 / 223

nums = [1,2,3,4,3]
test = Solution()
print(test.nextGreaterElements(nums))
