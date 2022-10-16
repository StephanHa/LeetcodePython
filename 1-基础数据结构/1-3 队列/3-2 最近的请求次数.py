# 933. 最近的请求次数（简单）
# https://leetcode.cn/problems/number-of-recent-calls/
#
# 写一个RecentCounter类来计算特定时间范围内最近的请求。
# 请实现 RecentCounter 类：
# RecentCounter() 初始化计数器，请求数为 0 。
# int ping(int t) 在时间 t 添加一个新请求，其中 t 表示以毫秒为单位的某个时间，并返回过去 3000 毫秒内发生的所有请求数（包括新请求）。确切地说，返回在 [t-3000, t] 内发生的请求数。
# 保证 每次对 ping 的调用都使用比之前更大的 t 值。
#
#
# 示例：
# 输入：
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# 输出：
# [null, 1, 2, 3, 3]
# 解释：
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // requests = [1]，范围是 [-2999,1]，返回 1
# recentCounter.ping(100);   // requests = [1, 100]，范围是 [-2900,100]，返回 2
# recentCounter.ping(3001);  // requests = [1, 100, 3001]，范围是 [1,3001]，返回 3
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002]，范围是 [2,3002]，返回 3
#
# 提示：保证每次对 ping 调用所使用的 t 值都 严格递增

# 方法1，队列
# 复杂度分析
# 1. 时间复杂度：O(1)
# 2. 空间复杂度：O(n)

import collections
class RecentCounter:

    def __init__(self):
        self.requests = collections.deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        start_time = t - 3000
        while self.requests[0] < start_time:
            self.requests.popleft()
        return len(self.requests)



# 执行用时：204 ms, 在所有 Python3 提交中击败了97.10%的用户
# 内存消耗：19.9 MB, 在所有 Python3 提交中击败了24.83%的用户
# 通过测试用例：68 / 68


