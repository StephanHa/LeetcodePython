# 122. 买卖股票的最佳时机 II（中等）
# 给你一个整数数组 prices ，其中prices[i] 表示某支股票第 i 天的价格。
# 在每一天，你可以决定是否购买和/或出售股票。你在任何时候最多只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。
# 返回 你能获得的 最大 利润。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 方法1，一次遍历
# 从第二天开始，只要比前一天大，就买入前一天，第二天卖出
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                result += prices[i] - prices[i-1]
        return result


# 执行用时：40 ms, 在所有 Python3 提交中击败了75.39%的用户
# 内存消耗：15.8 MB, 在所有 Python3 提交中击败了68.88%的用户
# 通过测试用例：200 / 200

