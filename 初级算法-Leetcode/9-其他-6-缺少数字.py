# 给定一个包含 [0, n]中n个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
#
# 示例 1：
#
# 输入：nums = [3,0,1]
# 输出：2
# 解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。

# 进阶：你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?

# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xnj4mt/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 方法1，集合
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n+1):
            if i not in set(nums):
                return i

# nums = [9,6,4,2,3,5,7,0,1]
nums = [0,1]
test = Solution()
print(test.missingNumber(nums))

# 执行用时：7368 ms, 在所有 Python3 提交中击败了5.04%的用户
# 内存消耗：16.5 MB, 在所有 Python3 提交中击败了5.01%的用户
# 通过测试用例：122 / 122



# 优化，减少每次遍历都将列表转换成集合的操作
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = set(nums)
        for i in range(n+1):
            if i not in result:
                return i

# 执行用时：36 ms, 在所有 Python3 提交中击败了95.50%的用户
# 内存消耗：16.4 MB, 在所有 Python3 提交中击败了9.02%的用户
# 通过测试用例：122 / 122



# 方法2，进阶要求
# 求和再相减
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        left = sum([i for i in range(n+1)])
        right = sum(nums)
        return left - right

# 执行用时：40 ms, 在所有 Python3 提交中击败了87.75%的用户
# 内存消耗：16.1 MB, 在所有 Python3 提交中击败了36.41%的用户
# 通过测试用例：122 / 122


from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        left = int(n * (n + 1) / 2) # 数学求和
        right = sum(nums)
        return left - right

# 执行用时：36 ms, 在所有 Python3 提交中击败了95.49%的用户
# 内存消耗：16 MB, 在所有 Python3 提交中击败了54.09%的用户
# 通过测试用例：122 / 122


# 下标与元素相同则存在，不同则不存在
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i != nums[i]:
                return i
        return n
    
# 执行用时：52 ms, 在所有 Python3 提交中击败了44.67%的用户
# 内存消耗：15.9 MB, 在所有 Python3 提交中击败了70.45%的用户
# 通过测试用例：122 / 122


