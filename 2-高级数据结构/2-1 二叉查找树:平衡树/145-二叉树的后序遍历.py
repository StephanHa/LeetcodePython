145 二叉树的后续遍历
https://leetcode.cn/problems/binary-tree-postorder-traversal/

给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。

输入：root = [1,null,2,3]
输出：[3,2,1]


方法1，迭代
关键点，右子树已遍历，需标记，用于说明其根节点的左右子树已遍历，可以添加其根节点的值
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if not root:
            return result

        stack = list()
        node = root
        prev = None # 右子树已遍历标记
        # 后序遍历
        # 先左子树，再右子树，最后根节点
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            # 如果右子树为空或者已经遍历过，则结果添加当前节点值
            if not node.right or node.right == prev:
                result.append(node.val)
                prev = node # 设置为当前遍历的节点
                node = None # 设置当前节点为None，是为了下次循环继续栈顶弹出
            # 如果右子树非空，则加入栈
            else:
                stack.append(node)
                node = node.right

        return result

执行用时：44 ms, 在所有 Python3 提交中击败了12.63%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了39.99%的用户
通过测试用例：68 / 68


方法2，递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traversal(root):
            if not root:
                return
            # 二叉树后序遍历
            traversal(root.left)
            traversal(root.right)
            result.append(root.val)

        result = list()
        traversal(root)
        return result

执行用时：44 ms, 在所有 Python3 提交中击败了12.63%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了5.02%的用户
通过测试用例：68 / 68


from typing import List
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
