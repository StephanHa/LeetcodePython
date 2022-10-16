# 36. 有效的数独 （中等）
# https://leetcode.cn/problems/valid-sudoku/
#
# 请你判断一个9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
# 数字1-9在每一行只能出现一次。
# 数字1-9在每一列只能出现一次。
# 数字1-9在每一个以粗实线分隔的3x3宫内只能出现一次。（请参考示例图）
#
# 注意：
# 一个有效的数独（部分已被填充）不一定是可解的。
# 只需要根据以上规则，验证已经填入的数字是否有效即可。
# 空白格用'.'表示。


# 方法1，一次遍历
# 每次遍历分别检查行、列和区域是否重复出现，重复则直接返回False，全部检查通过最后返回True
# 关键是区域如何用i行和j列号表示，areas[x] = i // m * m + j // m（m为边长平方根）
import math
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        len_board = len(board[0])
        m = int(math.sqrt(len_board))
        rows = [list() for i in range(len_board)]
        columns = [list() for i in range(len_board)]
        areas = [list() for i in range(len_board)]
        for i in range(len_board):
            for j in range(len_board):
                if board[i][j] == '.':
                    continue
                area = i // m * m + j // m
                if board[i][j] in rows[i] or board[i][j] in columns[j] or board[i][j] in areas[area]:
                    return False
                rows[i].append(board[i][j])
                columns[j].append(board[i][j])
                areas[area].append(board[i][j])

        return True

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

test = Solution()
print(test.isValidSudoku(board))


# 执行用时：40 ms, 在所有 Python3 提交中击败了93.29%的用户
# 内存消耗：15 MB, 在所有 Python3 提交中击败了58.66%的用户
# 通过测试用例：507 / 507

