# 给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；
# 如果数组中每个元素互不相同，返回 false 。
# 输入：nums = [1,2,3,1]
# 输出：true

# 方法1，借助哈希表
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashs = dict()
        for i in range(len(nums)):
            if nums[i] in hashs.keys():
                return True
            else:
                hashs[nums[i]] = 1
        return False


nums = [1,2,3,1]
# 输出：true
test = Solution()
print(test.containsDuplicate(nums))


# 执行用时：60 ms, 在所有 Python3 提交中击败了65.43%的用户
# 内存消耗：26.4 MB, 在所有 Python3 提交中击败了21.82%的用户
# 通过测试用例：70 / 70
