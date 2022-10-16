# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
# 注意：若s 和 t中每个字符出现的次数都相同，则称s 和 t互为字母异位词。
# 提示:
# 1 <= s.length, t.length <= 5 * 10^4
# s 和 t 仅包含小写字母

# 进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
#
# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xn96us/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ss = "".join(sorted(s))
        ts = "".join(sorted(t))
        if ss == ts:
            return True
        else:
            return False


s = "anagram"
t = "nagaram"
# 输出: true
test = Solution()
print(test.isAnagram(s, t))

# 执行用时：48 ms, 在所有 Python3 提交中击败了80.33%的用户
# 内存消耗：15.6 MB, 在所有 Python3 提交中击败了20.68%的用户
# 通过测试用例：37 / 37
