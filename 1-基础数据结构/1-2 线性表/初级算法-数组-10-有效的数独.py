# 请你判断一个9 x 9 的数独是否有效。只需要根据以下规则 ，验证已经填入的数字是否有效即可。
#
# 数字1-9在每一行只能出现一次。
# 数字1-9在每一列只能出现一次。
# 数字1-9在每一个以粗实线分隔的3x3宫内只能出现一次。（请参考示例图）
#
# 注意：
# 一个有效的数独（部分已被填充）不一定是可解的。
# 只需要根据以上规则，验证已经填入的数字是否有效即可。
# 空白格用'.'表示。
#
# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/x2f9gg/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 方法1，哈希表
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        rows = [dict() for _ in range(m)]
        columns = [dict() for _ in range(m)]
        areas = [dict() for _ in range(m)]
        for i in range(m):
            for j in range(m):
                target = board[i][j]
                if target == ".":
                    continue
                # 行i列j编号，与区域编号（0-8）之间的关系
                index = i // 3 * 3 + j // 3
                # 如果存在相同数字，则直接返回False
                if target in rows[i].keys() or target in columns[j].keys() or target in areas[index].keys():
                    return False
                # 否则，每个字典添加以数字为key的元素
                rows[i][target] = 0
                columns[j][target] = 0
                areas[index][target] = 0
        return True


board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
# 输出：true

# board = [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# 输出：false

# test = Solution()
# print(test.isValidSudoku(board))

# 执行用时：44 ms, 在所有 Python3 提交中击败了80.63%的用户
# 内存消耗：14.9 MB, 在所有 Python3 提交中击败了82.63%的用户
# 通过测试用例：507 / 507


# 方法2，集合
from typing import List
class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        rows = [set() for _ in range(m)]
        columns = [set() for _ in range(m)]
        areas = [set() for _ in range(m)]
        for i in range(m):
            for j in range(m):
                target = board[i][j]
                if target == ".":
                    continue
                # 行i列j编号，与区域编号（0-8）之间的关系
                index = i // 3 * 3 + j // 3
                # 如果存在相同数字，则直接返回False
                if target in rows[i] or target in columns[j] or target in areas[index]:
                    return False
                # 否则，每个字典添加以数字为key的元素
                rows[i].add(target)
                columns[j].add(target)
                areas[index].add(target)
        return True


test = Solution2()
print(test.isValidSudoku(board))


# 执行用时：48 ms, 在所有 Python3 提交中击败了61.71%的用户
# 内存消耗：14.9 MB, 在所有 Python3 提交中击败了75.31%的用户
# 通过测试用例：507 / 507

