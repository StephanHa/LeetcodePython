160 相交链表（简单）
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
https://leetcode.cn/problems/intersection-of-two-linked-lists/

方法1，
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodeA, nodeB = headA, headB
        while nodeA != nodeB:
            if nodeA:
                nodeA = nodeA.next
            else:
                nodeA = headB
            if nodeB:
                nodeB = nodeB.next
            else:
                nodeB = headA
        return nodeA
执行用时：140 ms, 在所有 Python3 提交中击败了84.56%的用户
内存消耗：30.1 MB, 在所有 Python3 提交中击败了14.07%的用户
通过测试用例：39 / 39


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
