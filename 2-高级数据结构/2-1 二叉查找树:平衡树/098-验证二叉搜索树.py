98 验证二叉搜索树（中等）
https://leetcode.cn/problems/validate-binary-search-tree

给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
有效 二叉搜索树定义如下：
节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。


方法1，中序遍历（迭代）
判断当前节点是否比前一个节点值大，大则继续，小或等于则放回False
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        pre_node = float('-inf')
        stack = list()
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.val <= pre_node:
                return False
            pre_node = node.val
            node = node.right
        return True

执行用时：48 ms, 在所有 Python3 提交中击败了70.52%的用户
内存消耗：17.6 MB, 在所有 Python3 提交中击败了56.86%的用户
通过测试用例：80 / 80



class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pre_node = float('-inf')
        stack = list()
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.val <= pre_node:
                return False
            pre_node = node.val
            node = node.right
        return True

执行用时：28 ms, 在所有 Python3 提交中击败了99.99%的用户
内存消耗：17.7 MB, 在所有 Python3 提交中击败了49.11%的用户
通过测试用例：80 / 80
