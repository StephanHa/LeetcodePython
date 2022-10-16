# 901. 股票价格跨度
# 编写一个 StockSpanner 类，它收集某些股票的每日报价，并返回该股票当日价格的跨度。
# 今天股票价格的跨度被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。
#
# 例如，如果未来7天股票的价格是 [100, 80, 60, 70, 60, 75, 85]，那么股票跨度将是 [1, 1, 1, 2, 1, 4, 6]。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/online-stock-span
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 输入：["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
# 输出：[null,1,1,1,2,1,4,6]
# 解释：
# 首先，初始化 S = StockSpanner()，然后：
# S.next(100) 被调用并返回 1，
# S.next(80) 被调用并返回 1，
# S.next(60) 被调用并返回 1，
# S.next(70) 被调用并返回 2，
# S.next(60) 被调用并返回 1，
# S.next(75) 被调用并返回 4，
# S.next(85) 被调用并返回 6。
#
# 注意 (例如) S.next(75) 返回 4，因为截至今天的最后 4 个价格
# (包括今天的价格 75) 小于或等于今天的价格。


class StockSpanner:

    def __init__(self):
        # 单调递减栈，元素为[price, count]
        self.stack = list()

    def next(self, price: int) -> int:
        count = 1
        # 栈非空并且今天报价比栈顶大，则出栈计算今天的跨度
        while self.stack and self.stack[-1][0] <= price:
            stock = self.stack.pop()
            count += stock[1]
        # 将小于今天的报价都出栈后，再将今天的入栈，维护一个递减栈
        self.stack.append([price, count])
        return count

# 执行用时：404 ms, 在所有 Python3 提交中击败了10.38%的用户
# 内存消耗：19.6 MB, 在所有 Python3 提交中击败了86.91%的用户
# 通过测试用例：99 / 99

test = StockSpanner()
print(test.next(100))
print(test.next(80))
print(test.next(60))
print(test.next(70))
print(test.next(60))
print(test.next(75))
print(test.next(85))
