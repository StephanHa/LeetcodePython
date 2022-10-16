# 498 对角线遍历（中等）
# https://leetcode.cn/problems/diagonal-traverse/
# 给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。

# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,4,7,5,3,6,8,9]

# 方法1，直接模拟
# https://leetcode.cn/problems/diagonal-traverse/solution/dui-jiao-xian-bian-li-by-leetcode-soluti-plz7/
# m行，n列，观察对角线遍历的规律，可以得到如下信息：
# 1、总共有（m+n-1)条对角线，相邻对角线的遍历方向不同
# 2、对角线从上到下的编号为i，范围[0, m+n-2]，i为偶数时从下往上遍历，i为奇数时从上往下遍历
# 3、（偶数）当第i条对角线从下往上遍历时，每次行索引减1，列索引加1，直到边缘
#   3.1 当i<m时，起始位置为（i,0）
#   3.2 当i>=m时，起始位置为（m-1,i-m+1）
# 4、（奇数）当第i条对角线从上往下遍历时，每次行索引加1，列索引减1，直到边缘
#   4.1 当i<n时，起始位置为（0,i）
#   4.2 当i>=n时，起始位置为（i-n+1, n-1）

# 复杂度分析
# 时间复杂度：O(m*n)，矩阵所有元素都需要遍历一次
# 空间复杂度：O(1)
from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(mat), len(mat[0])
        for i in range(m+n-1):
            if i % 2: # 奇数次数的对角线
                x = 0 if i < n else i-n+1
                y = i if i < n else n-1
                while x < m and y >= 0:
                    ans.append(mat[x][y])
                    x += 1
                    y -= 1
            else:  # 偶数次数的对角线
                x = i if i < m else m-1
                y = 0 if i < m else i-m+1
                while x >= 0 and y < n:
                    ans.append(mat[x][y])
                    x -= 1
                    y += 1

        return ans 


