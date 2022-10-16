# 你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。
# 由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。
# 假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。
# 你可以通过调用bool isBadVersion(version)接口来判断版本号 version 是否在单元测试中出错。
# 实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。
#
# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xnto1s/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# 方法1，二分查找
# min如果是错误，则继续往前查找；如果不是错误版本，则继续往后查找

# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    if version == 9:
        return True
    else:
        return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        result = n
        left, right = 1, n
        while left <= right:
            if left == right:
                return left
            min = (left + right) // 2
            if isBadVersion(min):
                right = min
            else:
                left = min + 1


n = 9
test = Solution()
print(test.firstBadVersion(n))

# 执行用时：36 ms, 在所有 Python3 提交中击败了65.90%的用户
# 内存消耗：14.9 MB, 在所有 Python3 提交中击败了38.56%的用户
# 通过测试用例：24 / 24
