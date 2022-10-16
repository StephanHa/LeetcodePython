# 209 长度最小的子数组（中等）
# https://leetcode.cn/problems/minimum-size-subarray-sum/
# 给定一个含有n个正整数的数组和一个正整数 target 。
# 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组[numsl, numsl+1, ..., numsr-1, numsr]，并返回其长度。
# 如果不存在符合条件的子数组，返回 0 。

# 方法1，滑动窗口
# https://leetcode.cn/problems/minimum-size-subarray-sum/solution/chang-du-zui-xiao-de-zi-shu-zu-by-leetcode-solutio/
# 复杂度分析
# 1. 时间复杂度：O(n)
# 2. 空间复杂度：O(1)

from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums or sum(nums) < target:
            return 0
        n = len(nums)
        result = n + 1
        start, end, sums = 0, 0, 0
        while end < n:
            sums += nums[end]
            while sums >= target:
                result = min(result, end - start + 1)
                sums -= nums[start]
                start += 1
            end += 1
        return 0 if result == n+1 else result


target = 7
nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。

test = Solution()
print(test.minSubArrayLen(target,nums))

# 执行用时：56 ms, 在所有 Python3 提交中击败了77.84%的用户
# 内存消耗：24.4 MB, 在所有 Python3 提交中击败了15.70%的用户
# 通过测试用例：20 / 20
