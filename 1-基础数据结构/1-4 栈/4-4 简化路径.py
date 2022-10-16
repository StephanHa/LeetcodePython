# 71 简化路径（中等）
# https://leetcode.cn/problems/simplify-path
# 给你一个字符串 path ，表示指向某一文件或目录的Unix 风格 绝对路径 （以 '/' 开头），
# 请你将其转化为更加简洁的规范路径。
# 在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..）表示将目录切换到上一级（指向父目录）；
# 两者都可以是复杂相对路径的组成部分。任意多个连续的斜杠（即，'//'）都被视为单个斜杠 '/' 。
# 对于此问题，任何其他格式的点（例如，'...'）均被视为文件/目录名称。
#
# 请注意，返回的 规范路径 必须遵循下述格式：
# 始终以斜杠 '/' 开头。
# 两个目录名之间必须只有一个斜杠 '/' 。
# 最后一个目录名（如果存在）不能 以 '/' 结尾。
# 此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 '.' 或 '..'）。
# 返回简化后得到的 规范路径 。

# 示例
# 输入：path = "/home/"
# 输出："/home"
# 解释：注意，最后一个目录名后面没有斜杠。
#
# 输入：path = "/home//foo/"
# 输出："/home/foo"
# 解释：在规范路径中，多个连续斜杠需要用一个斜杠替换。
#
# 输入：path = "/a/./b/../../c/"
# 输出："/c"


# 方法1，栈
# 对字符串以斜杆分割，再对字符item分类处理：
# （1）item为两个点，弹出栈顶元素
# （2）item非空且非一个点，压入栈
# （3）item为空或一个点，不处理

class Solution:
    def simplifyPath(self, path: str) -> str:
        strlist = path.split("/")
        stack = list()
        for item in strlist:
            if item == ".." and stack:
                stack.pop()
            elif item and item != '.':
                stack.append(item)
        return "/" + "/".join(stack)

# 执行用时：40 ms, 在所有 Python3 提交中击败了57.25%的用户
# 内存消耗：15.2 MB, 在所有 Python3 提交中击败了16.89%的用户
# 通过测试用例：257 / 257

path = "/a/./b/../../c/"
# 输出："/c"
test = Solution()
print(test.simplifyPath(path))

