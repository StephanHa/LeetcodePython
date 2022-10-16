# 155 最小栈
# https://leetcode.cn/problems/min-stack/
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
#
# 实现 MinStack 类:
# MinStack() 初始化堆栈对象。
# void push(int val) 将元素val推入堆栈。
# void pop() 删除堆栈顶部的元素。
# int top() 获取堆栈顶部的元素。
# int getMin() 获取堆栈中的最小元素。


# 方法1，数组（能实现功能，但没有达到常数时间内检索的要求）
class MinStack:
    def __init__(self):
        self.stack = list()

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)

# 执行用时：540 ms, 在所有 Python3 提交中击败了14.80%的用户
# 内存消耗：18.3 MB, 在所有 Python3 提交中击败了69.61%的用户
# 通过测试用例：31 / 31


# 方法2，二元数组（当前值, 当前最小值）
class MinStack2:
    def __init__(self):
        self.stack = list()

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# 执行用时：52 ms, 在所有 Python3 提交中击败了95.63%的用户
# 内存消耗：18.9 MB, 在所有 Python3 提交中击败了5.04%的用户
# 通过测试用例：31 / 31
