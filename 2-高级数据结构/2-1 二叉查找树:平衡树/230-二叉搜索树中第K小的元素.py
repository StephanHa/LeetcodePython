230. 二叉搜索树中第K小的元素（中等）
https://leetcode.cn/problems/kth-smallest-element-in-a-bst/

给定一个二叉搜索树的根节点root，和一个整数k，请你设计一个算法查找其中第k个最小元素（从1开始计数）。

进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？


方法1，中序遍历
二叉搜索树特点，中序遍历获得数组数值从小到大排序
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = list()
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right


执行用时：52 ms, 在所有 Python3 提交中击败了82.08%的用户
内存消耗：19 MB, 在所有 Python3 提交中击败了38.99%的用户
通过测试用例：93 / 93



方法2，平衡二叉搜索树（问题进阶）难懂
https://leetcode.cn/problems/kth-smallest-element-in-a-bst/solution/er-cha-sou-suo-shu-zhong-di-kxiao-de-yua-8o07/



