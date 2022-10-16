652. 寻找重复的子树
https://leetcode.cn/problems/find-duplicate-subtrees

给定一棵二叉树 root，返回所有重复的子树。
对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
如果两棵树具有相同的结构和相同的结点值，则它们是重复的。


方法1，深度优先搜索
https://leetcode.cn/problems/find-duplicate-subtrees/solution/xun-zhao-zhong-fu-de-zi-shu-by-leetcode/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        counts = dict()
        result = list()

        def collect(node):
            if not node: return "#"
            subtree = "{},{},{}".format(node.val, collect(node.left), collect(node.right))
            if subtree in counts.keys():
                counts[subtree] += 1
            else:
                counts[subtree] = 1
            if counts[subtree] == 2:
                result.append(node)
            return subtree

        collect(root)
        return result

执行用时：64 ms, 在所有 Python3 提交中击败了61.34%的用户
内存消耗：24.2 MB, 在所有 Python3 提交中击败了72.61%的用户
通过测试用例：176 / 176



