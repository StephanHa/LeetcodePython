# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
#
# 实现 MinStack 类:
# MinStack() 初始化堆栈对象。
# void push(int val) 将元素val推入堆栈。
# void pop() 删除堆栈顶部的元素。
# int top() 获取堆栈顶部的元素。
# int getMin() 获取堆栈中的最小元素。
#
# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xnkq37/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# class MinStack:
#
#     def __init__(self):
#
#
#     def push(self, val: int) -> None:
#
#
#     def pop(self) -> None:
#
#
#     def top(self) -> int:
#
#
#     def getMin(self) -> int:



class MinStack:
    def __init__(self):
        self.stack = list()

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val, val])
        else:
            self.stack.append([val, min(val, self.stack[-1][1])])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())    #--> 返回 -3.
minStack.pop()
print(minStack.top())       #--> 返回 0.
print(minStack.getMin())    #--> 返回 -2.


# 执行用时：48 ms, 在所有 Python3 提交中击败了98.65%的用户
# 内存消耗：18.7 MB, 在所有 Python3 提交中击败了12.10%的用户
# 通过测试用例：31 / 31

