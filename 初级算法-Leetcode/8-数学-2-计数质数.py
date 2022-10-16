# 给定整数 n ，返回 所有小于非负整数n的质数的数量 。
# 提示：0 <= n <= 5 * 10^6

# 示例 1：
# 输入：n = 10
# 输出：4
# 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
#
# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xnzlu6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# 方法1，质数倍数都是合数
# 质数（素数），大于1并只能被1和自己整除，质数的倍数都是合数
class Solution:
    def countPrimes(self, n: int) -> int:
        results = [1] * n  # 初始1表示为质数
        count = 0
        i = 2
        while i < n:
            if results[i] == 1:
                count += 1
                for j in range(i*i, n, i):
                    results[j] = 0
            i += 1
        return count

n = 2
test = Solution()
print(test.countPrimes(n))


# 执行用时：3828 ms, 在所有 Python3 提交中击败了45.67%的用户
# 内存消耗：53.1 MB, 在所有 Python3 提交中击败了44.36%的用户
# 通过测试用例：66 / 66
