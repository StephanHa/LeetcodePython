# 给定一个整数，写一个函数来判断它是否是 3的幂次方。如果是，返回 true ；否则，返回 false 。
# 整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x

# 提示：-2^31 <= n <= 2^31 - 1

# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xnsdi2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 方法1，暴力（超时）
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n % 3 == 0:
            n = n // 3
        return n == 1

# 方法2，集合存储所有3的幂
# 3 ** 20 > 2^31 - 1, 3 ** 19 < 2^31 - 1
class Solution:
    def isPowerOfThree(self, n):
        results = set(3**i for i in range(20))
        return n in results

# 执行用时：160 ms, 在所有 Python3 提交中击败了7.40%的用户
# 内存消耗：15 MB, 在所有 Python3 提交中击败了21.89%的用户
# 通过测试用例：21040 / 21040

