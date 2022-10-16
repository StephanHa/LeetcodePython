19. 删除链表的倒数第 N 个结点
https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
给定一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

输入：head = [1], n = 1
输出：[]

进阶：能尝试使用一趟扫描实现吗？

方法1，双指针
时间复杂度：O(L)，L为链表长度
空间复杂度：O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        dummy.next = head
        fast, slow = dummy, dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
执行用时：36 ms, 在所有 Python3 提交中击败了78.61%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了40.85%的用户
通过测试用例：208 / 208

参考：
https://leetcode.cn/problems/remove-nth-node-from-end-of-list/solution/shan-chu-lian-biao-de-dao-shu-di-nge-jie-dian-b-61/
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return dummy.next


方法2，栈
时间复杂度：O(L)
空间复杂度：O(L)
先遍历一次，将链表元素分别入栈，然后出栈n个元素，得到倒数第n个元素的前一个节点
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        stack = list()
        current_node = dummy
        while current_node:
            stack.append(current_node)
            current_node = current_node.next
        for _ in range(n):
            stack.pop()
        prev_node = stack[-1]
        prev_node.next = prev_node.next.next
        return dummy.next

执行用时：36 ms, 在所有 Python3 提交中击败了78.61%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了37.38%的用户
通过测试用例：208 / 208
