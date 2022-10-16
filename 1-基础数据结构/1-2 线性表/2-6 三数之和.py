# 15. 三数之和（中等）(非常经典面试题)
# https://leetcode.cn/problems/3sum
# 给你一个包含n个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，
# 使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。（排序，跳过相同值，达到去重）

# 方法1，排序+双指针
# https://leetcode.cn/problems/3sum/solution/san-shu-zhi-he-by-leetcode-solution/
# https://leetcode.cn/problems/3sum/solution/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/
# 复杂度分析
# 1、时间复杂度：O(n**2)
# 2、空间复杂度：O(log n)

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 排序+双指针
        result = list()
        nums = sorted(nums)
        n = len(nums)
        # 枚举i
        for i in range(n-2):
            # 跳过重复的元素
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            k = n - 1
            # 枚举j
            for j in range(i+1, n-1):
                # 跳过重复的元素
                if j > (i+1) and nums[j] == nums[j-1]:
                    continue
                while j < k and nums[j] + nums[k] > target:
                    k -= 1
                if j == k:
                    break
                if nums[j] + nums[k] == target:
                    result.append([nums[i], nums[j], nums[k]])
        return result


nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#
# 输入：nums = [0]
# 输出：[]

test = Solution()
print(test.threeSum(nums))

# 执行用时：644 ms, 在所有 Python3 提交中击败了68.66%的用户
# 内存消耗：17.8 MB, 在所有 Python3 提交中击败了89.97%的用户
# 通过测试用例：311 / 311
