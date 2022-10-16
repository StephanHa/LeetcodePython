# 20 有效的括号（简单）
# https://leetcode.cn/problems/valid-parentheses
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
# 示例：
# 输入：s = "()[]{}"
# 输出：true
#
# 输入：s = "([)]"
# 输出：false


# 方法1，栈（列表实现）
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")": "(", "]": "[", "}": "{"}
        stack = list()
        for x in s:
            # 栈非空并且为右括号，则判断与栈顶元素是否相同
            if stack and x in dic.keys():
                # 相同则弹出，否则返回False
                if stack[-1] == dic[x]:
                    stack.pop()
                else:
                    return False
            # 栈空，或非右括号，则入栈
            else:
                stack.append(x)
        # 符合有效字符串，栈必然为空，非空则返回False
        return not stack


# 执行用时：28 ms, 在所有 Python3 提交中击败了98.07%的用户
# 内存消耗：15 MB, 在所有 Python3 提交中击败了62.77%的用户
# 通过测试用例：92 / 92
