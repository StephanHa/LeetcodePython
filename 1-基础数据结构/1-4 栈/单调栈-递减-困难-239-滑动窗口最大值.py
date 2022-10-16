# 239. 滑动窗口最大值（困难）
# 给你一个整数数组 nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。
# 你只可以看到在滑动窗口内的 k个数字。滑动窗口每次只向右移动一位。
# 返回 滑动窗口中的最大值 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/sliding-window-maximum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 示例1
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# 方法1，暴力破解
# from typing import List
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         n = len(nums)
#         left, right = 0, k
#         result = [0 for _ in range(n - k + 1)]
#         while right < (n + 1):
#             num_max = max(nums[left:right])
#             result[left] = num_max
#             left += 1
#             right += 1
#         return result
#
# # 执行结果：超出时间限制


# 方法2，单调栈（双端队列，固定滑动窗口）
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = list()
        stack = list()  # index，数组元素的下标
        for i in range(len(nums)):
            # 栈底元素等于i-k，表示滑动窗口已满，弹出栈底元素（保证滑动窗口满足k个数量）
            if stack and stack[0] == (i-k):
                stack.pop(0)
            # 新加入元素，比栈顶元素对应的元素大，则出栈
            while stack and nums[i] > nums[stack[-1]]:
                stack.pop()
            stack.append(i)
            # 下标大于等于k-1，说明栈内元素已达到k个元素，开始记录每次遍历的最大值
            if i >= (k-1):
                result.append(nums[stack[0]])
        return result

# 执行用时：9316 ms, 在所有 Python3 提交中击败了21.74%的用户
# 内存消耗：27.4 MB, 在所有 Python3 提交中击败了87.87%的用户
# 通过测试用例：51 / 51

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
# 输出：[3,3,5,5,6,7]
test = Solution()
print(test.maxSlidingWindow(nums, k))
