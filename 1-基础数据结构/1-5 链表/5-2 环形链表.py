141 环形链表（简单）
https://leetcode.cn/problems/linked-list-cycle

给你一个链表的头节点 head ，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
如果链表中存在环 ，则返回 true 。 否则，返回 false 。

方法1，集合判断节点是否已遍历过
时间复杂度：O(n)
空间复杂度：O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        set_nodes = set()
        while head:
            if head in set_nodes:
                return True
            set_nodes.add(head)
            head = head.next
        return False

方法2，快慢指针
如果出现环，则快慢指针一定会重合
时间复杂度：O(n)
空间复杂度：O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_node = head
        fast_node = head
        # 快节点及其next节点非空，则继续遍历，如果为空都没找到，则返回False
        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
            if slow_node == fast_node:
                return True
        return False

执行用时：48 ms, 在所有 Python3 提交中击败了96.91%的用户
内存消耗：18.6 MB, 在所有 Python3 提交中击败了70.80%的用户
通过测试用例：21 / 21
