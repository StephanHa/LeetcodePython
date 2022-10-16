# 48. 旋转图像（中等）
# 给定一个 n×n 的二维矩阵matrix 表示一个图像。请你将图像顺时针旋转 90 度。
# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/rotate-image
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n <= 1:
            return
        # 1、行首尾两两交换
        top, bottom = 0, (n-1)
        while top < bottom:
            matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
            top += 1
            bottom -= 1
        # 2、以左上斜线（即，i=j）划分，两两交换
        for i in range(1,n):
            for j in range(0, n):
                if i == j:
                    break
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[7,4,1],[8,5,2],[9,6,3]]
test = Solution()
print(test.rotate(matrix))

# 执行用时：32 ms, 在所有 Python3 提交中击败了90.38%的用户
# 内存消耗：15 MB, 在所有 Python3 提交中击败了43.78%的用户
# 通过测试用例：21 / 21
