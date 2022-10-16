# 23. 合并K个升序链表
# https://leetcode.cn/problems/merge-k-sorted-lists/
# 给你一个链表数组，每个链表都已经按升序排列。
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。

# 示例：
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next=None

# 方法1，两两列表合并
# from typing import List, Optional
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         def mergeTwoList(lista, listb):
#             dummy = ListNode(0)
#             tail = dummy
#             heada, headb = lista, listb
#             while heada and headb:
#                 if heada.val < headb.val:
#                     tail.next = heada
#                     tail = tail.next
#                     heada = heada.next
#                 else:
#                     tail.next = headb
#                     tail = tail.next
#                     headb = headb.next
#             if not heada:
#                 tail.next = headb
#             else:
#                 tail.next = heada
#             return dummy.next

#         head = ListNode(0)
#         target = head.next
#         for list in lists:
#             if list:
#                 target = mergeTwoList(target, list)
#         return target

# 执行用时：2412 ms, 在所有 Python3 提交中击败了18.40%的用户
# 内存消耗：17.9 MB, 在所有 Python3 提交中击败了82.75%的用户
# 通过测试用例：133 / 133


# 方法2，链表值存入数组，数组排序后再组成链表返回
# 参考：https://leetcode.cn/problems/merge-k-sorted-lists/solution/23-he-bing-kge-sheng-xu-lian-biao-by-wo-6q7ji/
from typing import List, Optional
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        tamp_list = []
        for listx in lists:
            head = listx
            while head:
                tamp_list.append(head.val)
                head = head.next
        target_list = sorted(tamp_list)
        dummy = ListNode(0)
        head = dummy
        for item in target_list:
            head.next = ListNode(item)
            head = head.next
        return dummy.next

执行用时：68 ms, 在所有 Python3 提交中击败了87.19%的用户
内存消耗：18.6 MB, 在所有 Python3 提交中击败了33.64%的用户
通过测试用例：133 / 133

#######################################################


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)
        
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        # 如果index大于链表长度，则不会插入节点。
        if index > self.size:
            return
        new_node = ListNode(val)
        pre_node = self.head
        # 如果index小于0，则在头部插入节点。
        if index < 0:
            new_node.next = pre_node.next
            pre_node.next = new_node
        # index小于链表长度，如果等于链表长度，则添加到链表的末尾
        else:
            for _ in range(index):
                pre_node = pre_node.next
            new_node.next = pre_node.next
            pre_node.next = new_node
        self.size += 1

# lists = [[1,4,5],[1,3,4],[2,6]]
#lists = [[1,4,5],[0,3,9],[2,6,9]]
lists = [[2],[],[-1]]
# lists = [[2],[]]
target_lists = []
for list in lists:
    linkedList = MyLinkedList()
    for value in list:
        linkedList.addAtTail(value)
    target_lists.append(linkedList.head.next)

print(target_lists)

head = target_lists[0]
while head:
    print(head.val, end=" ")
    head =head.next

test23 = Solution()
result = test23.mergeKLists(target_lists)
print(result)


# lists = [[1,4,5],[1,3,4],[2,6]]
head = result
while head:
    print(head.val, end=" ")
    head = head.next

