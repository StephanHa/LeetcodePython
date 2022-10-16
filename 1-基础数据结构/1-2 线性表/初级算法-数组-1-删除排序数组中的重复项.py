# 26. 删除有序数组中的重复项（简单）
# 给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。
#
# 由于在某些语言中不能改变数组的长度，所以必须将结果放在数组nums的第一部分。更规范地说，如果在删除重复项之后有 k 个元素，那么nums的前 k 个元素应该保存最终结果。
# 将最终结果插入nums 的前 k 个位置后返回 k 。
# 不要使用额外的空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/remove-duplicates-from-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 方法1，双指针
# 由于数组已排序，并且有重复项，去除后必然比之前的短
# 以index表示去重的数组的下标，遍历原数组，遇到不同时，index加入并存入当前元素
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        n = len(nums)
        index = 0

        for i in range(1, n):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]
        return index + 1


# 执行用时：44 ms, 在所有 Python3 提交中击败了60.82%的用户
# 内存消耗：15.9 MB, 在所有 Python3 提交中击败了91.93%的用户
# 通过测试用例：361 / 361

