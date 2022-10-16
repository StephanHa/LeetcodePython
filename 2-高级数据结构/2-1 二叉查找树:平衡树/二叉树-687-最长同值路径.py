# 687. 最长同值路径（中等）
# 给定一个二叉树的root，返回最长的路径的长度 ，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
# 两个节点之间的路径长度由它们之间的边数表示。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/longest-univalue-path
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# https://leetcode.cn/problems/longest-univalue-path/solution/zui-chang-tong-zhi-lu-jing-by-leetcode-s-hgfk/
# 方法1，递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            sub_left = dfs(node.left)
            sub_right = dfs(node.right)
            # 分别计算左右子树的同值长度
            if node.left and node.left.val == node.val:
                left = sub_left + 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right = sub_right + 1
            else:
                right = 0
            nonlocal result
            result = max(result, left + right)
            return max(left, right)
        dfs(root)
        return result

# 执行用时：320 ms, 在所有 Python3 提交中击败了77.02%的用户
# 内存消耗：19.1 MB, 在所有 Python3 提交中击败了68.18%的用户
# 通过测试用例：71 / 71
