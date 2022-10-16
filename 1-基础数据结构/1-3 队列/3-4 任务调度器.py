621 任务调度器（中等）
https://leetcode.cn/problems/task-scheduler/

给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。
然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
你需要计算完成所有任务所需要的 最短时间 。

示例：
输入：tasks = ["A","A","A","B","B","B"], n = 2
输出：8
解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B
     在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。 

方法1，构造
在任意的情况下，需要的最少时间就是 （maxExec - 1）*（n + 1）+maxCount和|task|中的较大值。
https://leetcode.cn/problems/task-scheduler/solution/ren-wu-diao-du-qi-by-leetcode-solution-ur9w/

import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        # 最多的执行次数
        maxExec = max(freq.values())
        # 具有最多执行次数的任务数量
        maxCount = sum(1 for v in freq.values() if v == maxExec)
        return max((maxExec-1)*(n+1)+maxCount, len(tasks))


# 不使用队列，直接使用数组
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [tasks.count(x) for x in set(tasks)]
        # 最多的执行次数
        maxExec = max(freq)
        # 具有最多执行次数的任务数量
        maxCount = freq.count(maxExec)
        return max((maxExec-1)*(n+1)+maxCount, len(tasks))

执行用时：88 ms, 在所有 Python3 提交中击败了39.47%的用户
内存消耗：17.3 MB, 在所有 Python3 提交中击败了14.00%的用户
通过测试用例：71 / 71











