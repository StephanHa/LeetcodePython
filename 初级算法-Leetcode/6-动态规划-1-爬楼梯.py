# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# https://leetcode.cn/leetbook/read/top-interview-questions-easy/xn854d/
# 输入：n = 3
# 输出：3
# 解释：有三种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶 + 1 阶
# 2. 1 阶 + 2 阶
# 3. 2 阶 + 1 阶

# 提示：1 <= n <= 45


# 方法1，数学规律
# n=1, 1; n=2, 2; n=3, 3; n=4, 2+3; ...
# 从n=4开始，都是前两个之和
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        if n <= 3:
            return n
        result = [1, 2, 3]
        for i in range(4, n+1):
            result.append(result[-2] + result[-1])
        return result[-1]

test = Solution()
print(test.climbStairs(3))

# 执行用时：32 ms, 在所有 Python3 提交中击败了87.58%的用户
# 内存消耗：14.8 MB, 在所有 Python3 提交中击败了82.05%的用户
# 通过测试用例：45 / 45


# 方法2，递归
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        if n <= 3:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)

test = Solution()
print(test.climbStairs(5))
# 执行结果：超出时间限制
# 最后执行的输入：44


# 方法3，动态规划
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [0 for _ in range(n+1)] # dp[i]表示i个台阶时的方法数量
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1] # 状态转移公式
        return dp[n]

