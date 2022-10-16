# 给你两个整数数组nums1 和 nums2 ，请你以数组形式返回两数组的交集。返回结果中每个元素出现的次数，
# 应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。
#
# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/x2y0c2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 进阶：
# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果nums1的大小比nums2 小，哪种方法更优？
# 如果nums2的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

# 方法1，排序+双指针
from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = list()
        nums1.sort()
        nums2.sort()
        i1, i2 = 0, 0
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] == nums2[i2]:
                result.append(nums1[i1])
                i1 += 1
                i2 += 1
            elif nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                i2 += 1
        return result


nums1 = [1,2,3,2]
nums2 = [1,4,2]
test = Solution()
print(test.intersect(nums1, nums2))

# 执行用时：36 ms, 在所有 Python3 提交中击败了85.73%的用户
# 内存消耗：15.1 MB, 在所有 Python3 提交中击败了38.36%的用户
# 通过测试用例：56 / 56
