# 54. 螺旋矩阵（中等）
# https://leetcode.cn/problems/spiral-matrix/

# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]

# 提示：
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

# 方法1，按层模拟
# https://leetcode.cn/problems/spiral-matrix/solution/luo-xuan-ju-zhen-by-leetcode-solution/
# 将矩阵看成若干层，首先输出最外层的元素，其次输出次外层的元素，直到输出最内层的元素。
# 对于每层，从左上方开始以顺时针的顺序遍历所有元素。
# 假设当前层的左上角位于（top, left），右下角位于（bottom，right），按照如下顺序遍历当前层的元素：

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 矩阵为空，或列为空，直接返回空列表
        if not matrix or not matrix[0]:
            return list()
        rows, columns = len(matrix), len(matrix[0])
        order = list()
        top, left = 0, 0 # 行、列左上角序号
        bottom, right = rows-1, columns-1  # 行、列右下角序号
        while left <= right and top <= bottom:
            # 上侧，top行固定，列遍历
            for column in range(left, right+1):
                order.append(matrix[top][column])
            # 右侧，right列固定，行遍历
            for row in range(top+1, bottom+1):
                order.append(matrix[row][right])
            if left < right and top < bottom:
                # 下侧，bottom行固定，列遍历
                for column in range(right-1, left, -1):
                    order.append(matrix[bottom][column])
                # 左侧，left列固定，行遍历
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            top, left = top+1, left+1
            bottom, right = bottom-1, right-1
        return order






class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = list()
        if not matrix or not matrix[0]:
            return result
        # 行
        top, bottom = 0, len(matrix) - 1
        # 列
        left, right = 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            # 上侧，top行固定，列遍历
            for column in range(left, right+1):
                result.append(matrix[top][column])
            # 右侧，right列固定，行遍历
            for row in range(top+1, bottom+1):
                result.append(matrix[row][right])
            if left < right and top < bottom:
                # 下侧，bottom行固定，列遍历
                for column in range(right-1, left, -1):
                    result.append(matrix[bottom][column])
                # 左侧，left列固定，行遍历
                for row in range(bottom, top, -1):
                    result.append(matrix[row][left])
            # 矩形外层减少1层
            top, bottom = top + 1, bottom - 1
            left, right = left + 1, right - 1
        return result


# 执行用时：28 ms, 在所有 Python3 提交中击败了97.20%的用户
# 内存消耗：14.9 MB, 在所有 Python3 提交中击败了75.00%的用户
# 通过测试用例：23 / 23
