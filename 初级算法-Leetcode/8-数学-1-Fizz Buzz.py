# 给你一个整数 n ，找出从 1 到 n 各个整数的 Fizz Buzz 表示，并用字符串数组 answer（下标从 1 开始）返回结果，其中：
#
# answer[i] == "FizzBuzz" 如果 i 同时是 3 和 5 的倍数。
# answer[i] == "Fizz" 如果 i 是 3 的倍数。
# answer[i] == "Buzz" 如果 i 是 5 的倍数。
# answer[i] == i （以字符串形式）如果上述条件全不满足。

# 提示：1 <= n <= 10^4

# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xngt85/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 方法1，直接模拟
from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [""] * (n+1)
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                answer[i] = "FizzBuzz"
            elif i % 3 == 0:
                answer[i] = "Fizz"
            elif i % 5 == 0:
                answer[i] = "Buzz"
            else:
                answer[i] = str(i)
        return answer[1:]

n = 15
test = Solution()
print(test.fizzBuzz(n))


# 执行用时：36 ms, 在所有 Python3 提交中击败了80.73%的用户
# 内存消耗：15.6 MB, 在所有 Python3 提交中击败了22.64%的用户
# 通过测试用例：8 / 8

