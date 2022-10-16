# 67. 二进制求和（简单）
# https://leetcode.cn/problems/add-binary/
# 给你两个二进制字符串，返回它们的和（用二进制表示）。
# 输入为 非空 字符串且只包含数字 1 和 0。

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = int(a, 2) + int(b, 2)
        return bin(result)[2:]


# 示例1
a = "11"
b = "1"
# 输出: "100"
test = Solution()
print(test.addBinary(a, b))

# 执行用时：28 ms, 在所有 Python3 提交中击败了98.56%的用户
# 内存消耗：14.8 MB, 在所有 Python3 提交中击败了97.60%的用户
# 通过测试用例：294 / 294


# 进制转换
#  https://blog.csdn.net/qq_46119688/article/details/122640639?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522166157270416782395383270%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=166157270416782395383270&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-2-122640639-null-null.142^v42^pc_rank_34_queryrelevant25,185^v2^control&utm_term=进制转换%20Python&spm=1018.2226.3001.4187
# 二、八、十六进制转十进制
# int(str_x, 2/8/16)

# 十进制转二、八、十六进制
# bin(num)
# oct(num)
# hex(num)

# format函数转换（x为其他进制数）
# format(x, 'b') 转为二进制
# format(x, 'o') 转为八进制
# format(x, 'd') 转为十进制
# format(x, 'x') 转为十六进制
