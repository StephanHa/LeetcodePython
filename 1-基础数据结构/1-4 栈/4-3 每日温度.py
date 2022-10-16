# 739 每日温度
# https://leetcode.cn/problems/daily-temperatures
# 给定一个整数数组temperatures，表示每天的温度，返回一个数组answer，其中answer[i]是指对于第 i 天，
# 下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用0 来代替。
#
# 示例：
# 输入: temperatures = [73,74,75,71,69,72,76,73]
# 输出: [1,1,4,2,1,1,0,0]


# 方法1，单调栈
# https://leetcode.cn/problems/daily-temperatures/solution/mei-ri-wen-du-by-leetcode-solution/
# 可以维护一个存储下标的单调栈，从栈底到栈顶的下标对应的温度列表中的温度依次递减。如果一个下标在单调栈里，则表示尚未找到下一次温度更高的下标。

from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        stack = list()  # 单调栈，存储元素是字符串的下标
        answer = [0 for _ in range(length)]
        for i in range(length):
            # 栈非空，当前数组元素比栈顶下标对应的元素大，则弹出再继续比较
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack[-1]
                answer[index] = i - index
                stack.pop()
            stack.append(i)
        # 栈非空，说明未找到第一个温度高的一天，默认为0
        return answer

# 注意：
# 判别是否需要使用单调栈，如果需要找到左边或者右边第一个比当前位置的数大或者小，则可以考虑使用单调栈；单调栈的题目如矩形米面积等等

# 单调栈，相关题目：
# 496 下一个更大元素I
# 901 股票价格跨度
# 042 接雨水
# 084 柱状图中最大的矩形

