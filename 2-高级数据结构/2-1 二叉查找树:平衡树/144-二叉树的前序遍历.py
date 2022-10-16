144 二叉树的前序遍历
https://leetcode.cn/problems/binary-tree-preorder-traversal/

给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

输入：root = [1,null,2,3]
输出：[1,2,3]

二叉树的中序遍历相关：
094 二叉树的中序遍历
144 二叉树的前序遍历
145 二叉树的后序遍历


方法1，递归
二叉树前序、中序、后序遍历的常用方法
时间复杂度：O(n)，n为二叉树的节点数
空间复杂度：O(n)，递归过程中栈的开销
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traversal(root):
            if not root: 
                return
            # 二叉树前序遍历
            result.append(root.val)
            traversal(root.left)
            traversal(root.right)

        result = list()
        traversal(root)
        return result

执行用时：32 ms, 在所有 Python3 提交中击败了89.44%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了41.29%的用户
通过测试用例：69 / 69


方法2，迭代
时间和空间复杂度，同上
递归是隐性的维护一个栈，迭代是显性维护一个栈
https://leetcode.cn/problems/binary-tree-preorder-traversal/solution/er-cha-shu-de-qian-xu-bian-li-by-leetcode-solution/
from typing import List
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        # 如果根节点为空，则直接返回空数组
        if not root:
            return result
        # 栈用数组实现，记录数节点，再弹出后遍历右子树
        stack = list()
        node = root
        # 前序遍历
        # 先根节点，再左子树，最后右子树
        while stack or node:
            while node:
                # 先记录根节点值
                result.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

        return result

执行用时：32 ms, 在所有 Python3 提交中击败了89.44%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了61.99%的用户
通过测试用例：69 / 69



方法3，Morris遍历
时间复杂度：O(n)
空间复杂度：O(1)




