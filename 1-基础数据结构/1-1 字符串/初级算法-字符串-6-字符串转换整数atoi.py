# 中等
# 请你来实现一个myAtoi(string s)函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。
# 函数myAtoi(string s) 的算法如下：
# 读入字符串并丢弃无用的前导空格
# 检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。确定最终结果是负数还是正数。如果两者都不存在，则假定结果为正。
# 读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
# 将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
# 如果整数数超过 32 位有符号整数范围 [−2^31, 2^31− 1] ，需要截断这个整数，使其保持在这个范围内。
# 具体来说，小于 −2^31 的整数应该被固定为 −2^31 ，大于 2^31− 1 的整数应该被固定为 2^31− 1 。
# 返回整数作为最终结果。

# 注意：
# 本题中的空白字符只包括空格字符 ' ' 。
# 除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。
#
# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xnoilh/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 方法1，直接模拟
class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        # 1、跳过无用的前导空格
        while i < n and s[i] == " ":
            i += 1
        # 2、读取+/-符号
        flag = ""
        if i < n and (s[i] == "-" or s[i] == "+"):
            flag = s[i]
            i += 1
        # 3、读取数字，遇到非数字则终止
        result = ""
        while i < n:
            if s[i].isdigit():
                result += s[i]
                i += 1
            else:
                break
        # 判断1、如果没有读入数字，则整数为0
        if len(result) == 0:
            return 0
        # 判断2，是否在有效范围内
        minnum = -2**31
        maxnum = 2**31 - 1
        result = int(flag + result)
        if result < minnum:
            return minnum
        if result > maxnum:
            return maxnum
        return result

# 执行用时：44 ms, 在所有 Python3 提交中击败了45.38%的用户
# 内存消耗：15 MB, 在所有 Python3 提交中击败了54.51%的用户
# 通过测试用例：1082 / 1082


# 方法2，优化
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip() # 去除左边空格
        if not s:
            return 0
        flag = 1
        if s[0] == "-":
            flag = -1
        if flag == -1 or s[0] == "+":
            s = s[1:]
        result = 0
        for item in s:
            if item.isdigit():
                result *= 10
                result += int(item)
            else:
                break
        return max(-2**31, min(2**31-1, flag*result))


s = "-91283472332"
# 输出：-2147483648
test = Solution()
print(test.myAtoi(s))

# 执行用时：40 ms, 在所有 Python3 提交中击败了70.10%的用户
# 内存消耗：15 MB, 在所有 Python3 提交中击败了36.71%的用户
# 通过测试用例：1082 / 1082
