# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 请注意，必须在不复制数组的情况下原地对数组进行操作。
# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/x2ba4i/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 方法1，快慢指针
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # 左指针指向待写入位置，右指针指向非0的位置
        left, right = 0, 0
        while right < n:
            # 当right下标值非0，则写入数组left下标的位置，然后left和right分别向后移动一位
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
                right += 1
            else: # 如果right下标值为0，则向后移动一位
                right += 1
        # 如果left < n，说明left当前及其后面下标的值都为0
        while left < n:
            nums[left] = 0
            left += 1
        return nums


nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]
test = Solution()
print(test.moveZeroes(nums))

# 执行用时：44 ms, 在所有 Python3 提交中击败了91.96%的用户
# 内存消耗：15.7 MB, 在所有 Python3 提交中击败了91.57%的用户
# 通过测试用例：74 / 74
