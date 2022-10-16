# 6. Z 字形变换 （中等）
# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
# https://leetcode.cn/problems/zigzag-conversion/

# 方法1，直接模拟
# 以指定行数生成字符串的数组，遍历字符串，对应行加入到相应下标的数组中
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = ["" for _ in range(numRows)]
        flag = -1
        i = 0
        for item in s:
            if i == 0 or i == (numRows - 1):
                flag = -flag
            result[i] += item
            i += flag
        return "".join(result)


s = "PAYPALISHIRING"
numRows = 3
# 输出："PAHNAPLSIIGYIR"

# s = "PAYPALISHIRING"
# numRows = 4
# 输出："PINALSIGYAHRPI"

test = Solution()
print(test.convert(s, numRows))


# 执行用时：48 ms, 在所有 Python3 提交中击败了95.16%的用户
# 内存消耗：15.1 MB, 在所有 Python3 提交中击败了62.74%的用户
# 通过测试用例：1157 / 1157
