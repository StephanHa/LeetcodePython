142 环形链表2（中等）
https://leetcode.cn/problems/linked-list-cycle-ii

给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
不允许修改 链表。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

方法1，集合判断节点是否已遍历，如果有环，返回第一个重复遍历的结点，否则返回null
时间复杂度：O(n)
空间复杂度：O(n)

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        set_nodes = set()
        while head:
            if head in set_nodes:
                return head
            set_nodes.add(head)
            head = head.next
        return head

执行用时：56 ms, 在所有 Python3 提交中击败了55.16%的用户
内存消耗：19.1 MB, 在所有 Python3 提交中击败了7.75%的用户
通过测试用例：16 / 16


方法2，双指针，一快一慢的指针，如果有环则必然重合
https://leetcode.cn/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/
时间复杂度：O(n)
空间复杂度：O(1)

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while fast:
            slow = slow.next
            # 如果fast下个节点为空，则直接返回空
            if not fast.next:
                return fast.next
            fast = fast.next.next
            # 如果fast和slow出现相等，则说明有环
            if fast == slow:
                target = head
                # 新指针从头开始，每次走一步，slow继续行走，第一次相等时，就是环的起始节点
                # 两指针重合，并同时指向链表环入口
                while target != slow:
                    target = target.next
                    slow = slow.next
                return target
        # 如果没有环，则fast必然走到链尾，链尾为空直接返回
        return fast

执行用时：44 ms, 在所有 Python3 提交中击败了97.32%的用户
内存消耗：18.7 MB, 在所有 Python3 提交中击败了26.55%的用户
通过测试用例：16 / 16