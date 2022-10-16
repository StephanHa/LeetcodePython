# 150 逆波兰表达式求值
# https://leetcode.cn/problems/evaluate-reverse-polish-notation
#
# 根据 逆波兰表示法，求表达式的值。
# 有效的算符包括+、-、*、/。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
# 注意两个整数之间的除法只保留整数部分。
# 可以保证给定的逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
#
# 示例：
# 输入：tokens = ["2","1","+","3","*"]
# 输出：9
# 解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
#
# 输入：tokens = ["4","13","5","/","+"]
# 输出：6
# 解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6

# 逆波兰表达式是一种后缀表达式，所谓后缀就是指算符写在后面。
# 平常使用的算式则是一种中缀表达式，如 ( 1 + 2 ) * ( 3 + 4 ) 。
# 该算式的逆波兰表达式写法为 ( ( 1 2 + ) ( 3 4 + ) * ) 。
#
# 逆波兰表达式主要有以下两个优点：
# 去掉括号后表达式无歧义，上式即便写成 1 2 + 3 4 + * 也可以依据次序计算出正确结果。
# 适合用栈操作运算：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中


# 方法1，栈（逆波兰表达式优点）
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()  # 栈元素为整数
        for item in tokens:
            if item == "+" or item == "-" or item == "*" or item == "/":
                y = int(stack.pop())
                x = int(stack.pop())
                if item == "+": result = x + y
                if item == "-": result = x - y
                if item == "*": result = x * y
                # 两个整数之间的除法只保留整数部分
                if item == "/": result = int(x / y)
                stack.append(result)
            else:
                stack.append(int(item))
        # 在保证给定的逆波兰表达式总是有效的前提下，求值后栈只剩下最终结果
        return stack[0]

# 执行用时：32 ms, 在所有 Python3 提交中击败了99.06%的用户
# 内存消耗：16.5 MB, 在所有 Python3 提交中击败了52.03%的用户
# 通过测试用例：20 / 20
