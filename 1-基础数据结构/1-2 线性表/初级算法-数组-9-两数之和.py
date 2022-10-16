# 给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，
# 并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。
# 进阶：你可以想出一个时间复杂度小于 O(n*n) 的算法吗？

# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/x2jrse/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 方法1，哈希表（key为元素，value为下标）
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashs = dict()
        for i in range(n):
            key = target - nums[i]
            if key in hashs.keys():
                return [hashs[key], i]
            hashs[nums[i]] = i


nums = [2,7,11,15]
target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
# test = Solution()
# print(test.twoSum(nums, target))

# 执行用时：36 ms, 在所有 Python3 提交中击败了88.91%的用户
# 内存消耗：16.1 MB, 在所有 Python3 提交中击败了19.00%的用户
# 通过测试用例：57 / 57


# 方法2，双指针
from typing import List
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = sorted(nums)
        i, j = 0, len(new_nums)-1
        while i < j:
            temp = new_nums[i] + new_nums[j]
            if temp == target:
                left, right = new_nums[i], new_nums[j]
            if temp < target:
                i += 1
            else:
                j -= 1
        return [nums.index(left), nums.index(right)]
        # 有缺陷，如果两个元素相同，查找到的所有都是第一个???
        # nums = [3,3], target = 6

test2 = Solution2()
print(test2.twoSum(nums, target))
