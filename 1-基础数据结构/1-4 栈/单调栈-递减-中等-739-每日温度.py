# 739. 每日温度（中等）
# 给定一个整数数组temperatures，表示每天的温度，返回一个数组answer，其中answer[i]是指对于第 i 天，
# 下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用0 来代替。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/daily-temperatures
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 方法1，单调递减栈
# 正向遍历温度数组，入栈则未找到更高温度，出栈则表示当前遍历值为其更高温度
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0 for _ in range(n)]  # 初始值为0，默认更高温度未找到
        stack = list()  # (value, index)
        for i in range(n):
            while stack and stack[-1][0] < temperatures[i]:
                day = stack.pop()
                result[day[1]] = i - day[1]
            stack.append((temperatures[i], i))
        return result

# 执行用时：240 ms, 在所有 Python3 提交中击败了38.18%的用户
# 内存消耗：23.5 MB, 在所有 Python3 提交中击败了5.01%的用户
# 通过测试用例：47 / 47

# 优化：入栈的元素为数组的元素下标，而非元素值+元素下标
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0 for _ in range(n)]  # 初始值为0，默认更高温度未找到
        stack = list()  # (index)
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        return result

# 执行用时：208 ms, 在所有 Python3 提交中击败了63.37%的用户
# 内存消耗：22.4 MB, 在所有 Python3 提交中击败了14.64%的用户
# 通过测试用例：47 / 47
