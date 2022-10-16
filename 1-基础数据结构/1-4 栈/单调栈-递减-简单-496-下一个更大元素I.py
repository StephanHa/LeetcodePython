# 496. 下一个更大元素 I（简单）
# nums1中数字x的 下一个更大元素 是指x在nums2 中对应位置 右侧 的 第一个 比x大的元素。
# 给你两个 没有重复元素 的数组nums1 和nums2 ，下标从 0 开始计数，其中nums1是nums2的子集。
# 对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，
# 并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。
# 返回一个长度为nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/next-greater-element-i
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 示例1
# 输入：nums1 = [4,1,2], nums2 = [1,3,4,2].
# 输出：[-1,3,-1]
# 解释：nums1 中每个值的下一个更大元素如下所述：
# - 4 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
# - 1 ，用加粗斜体标识，nums2 = [1,3,4,2]。下一个更大元素是 3 。
# - 2 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。

# 进阶：你可以设计一个时间复杂度为 O(nums1.length + nums2.length) 的解决方案吗？

# 方法1，单调递减栈+哈希表（字典）
# 由于nums1和nums2没有重复元素，则可以作为哈希表的key，value存储下一个更大元素
# 单调递减栈，只需遍历一次nums2，获取一下个更大元素
# 遍历一次nums1，从上一步获取的字典中，查找结果
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = list()
        temp = dict()
        # 先遍历nums2，查找每个元素的下一个更大元素
        for num in nums2:
            while stack and stack[-1] < num:
                node = stack.pop()
                temp[node] = num
            stack.append(num)
        # 栈为空，说明不存在下一个更大元素，value都为-1
        while stack:
            node = stack.pop()
            temp[node] = -1
        # 遍历nums1，查找temp哈希表获取每个元素的下个更大元素值
        result = list()
        for i in nums1:
            result.append(temp[i])
        return result


# 时间复杂度：O(len(nums1) + len(nums2))
# 空间复杂度：存储nums2的栈和哈希表

# 执行用时：36 ms, 在所有 Python3 提交中击败了87.56%的用户
# 内存消耗：15.1 MB, 在所有 Python3 提交中击败了43.20%的用户
# 通过测试用例：15 / 15

nums1 = [4,1,2]
nums2 = [1,3,4,2]
test = Solution()
print(test.nextGreaterElement(nums1, nums2))
