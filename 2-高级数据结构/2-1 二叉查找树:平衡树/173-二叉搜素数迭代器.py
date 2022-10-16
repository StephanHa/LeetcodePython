173 二叉搜索树迭代器（中等）
https://leetcode.cn/problems/binary-search-tree-iterator

实现一个二叉搜索树迭代器类BSTIterator ，表示一个按中序遍历二叉搜索树（BST）的迭代器：
BSTIterator(TreeNode root) 初始化 BSTIterator 类的一个对象。BST 的根节点 root 会作为构造函数的一部分给出。指针应初始化为一个不存在于 BST 中的数字，且该数字小于 BST 中的任何元素。
boolean hasNext() 如果向指针右侧遍历存在数字，则返回 true ；否则返回 false 。
int next()将指针向右移动，然后返回指针处的数字。
注意，指针初始化为一个不存在于 BST 中的数字，所以对 next() 的首次调用将返回 BST 中的最小元素。

你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 的中序遍历中至少存在一个下一个数字。


方法1，中序遍历提前保存一个数组
初始化时先进行中序遍历获取结果组成数组，next函数返回数组的当前索引对应的值，hasNext函数判断当前索引是否小于结果数组的长度
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.result = list()
        self.inorderTraversal(self.root)
        self.index = 0

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = list()
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            self.result.append(node.val)
            node = node.right

    def next(self) -> int:
        if self.index < len(self.result):
            next_node_val = self.result[self.index]
            self.index += 1
            return next_node_val

    def hasNext(self) -> bool:
        return self.index < len(self.result)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

执行用时：68 ms, 在所有 Python3 提交中击败了97.51%的用户
内存消耗：22.2 MB, 在所有 Python3 提交中击败了5.05%的用户
通过测试用例：61 / 61



方法2，单调栈
https://leetcode.cn/problems/binary-search-tree-iterator/solution/fu-xue-ming-zhu-dan-diao-zhan-die-dai-la-dkrm/







