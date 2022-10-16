94 二叉树的中序遍历
https://leetcode.cn/problems/binary-tree-inorder-traversal/

给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

输入：root = [1,null,2,3]
输出：[1,3,2]


方法1，迭代
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if not root:
            return result

        stack = list()
        node = root
        # 中序遍历
        # 先左子树，再根节点，最后右子树
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            # 无左子树，则弹出栈顶的数节点，并记录结果
            node = stack.pop()
            result.append(node.val)
            node = node.right
        
        return result

执行用时：32 ms, 在所有 Python3 提交中击败了89.70%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了80.29%的用户
通过测试用例：70 / 70

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        stack = list()
        node = root
        # 中序遍历（迭代）
        # 先左子树，再根节点，最后右子树
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            # 无左子树，则弹出栈顶的数节点，并记录结果
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result

执行用时：44 ms, 在所有 Python3 提交中击败了13.18%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.18%的用户
通过测试用例：70 / 70


方法2，递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traversal(root):
            if not root:
                return
            # 二叉树中序遍历
            traversal(root.left)
            result.append(root.val)
            traversal(root.right)

        result = list()
        traversal(root)
        return result

执行用时：36 ms, 在所有 Python3 提交中击败了70.06%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了5.18%的用户
通过测试用例：70 / 70

