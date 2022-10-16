707. 设计链表（中等）
https://leetcode.cn/problems/design-linked-list

设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next 是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。

在链表类中实现这些功能：
get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。

示例：
MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
linkedList.get(1);            //返回2
linkedList.deleteAtIndex(1);  //现在链表是1-> 3
linkedList.get(1);            //返回3

方法1，单向链表
https://leetcode.cn/problems/design-linked-list/solution/she-ji-lian-biao-by-leetcode/
时间复杂度：addAtHead O(1)，addAtTail O(n)，addAtIndex、get、deletAtIndex O(k)
空间复杂度：O(n)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0) # 哨兵节点，用作伪头始终存在

    # 注意，题目的index从0开始
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(index+1):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(-1, val)

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

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        pre_node = self.head
        for _ in range(index):
            pre_node = pre_node.next
        pre_node.next = pre_node.next.next
        self.size -= 1

执行用时：160 ms, 在所有 Python3 提交中击败了65.32%的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了49.97%的用户
通过测试用例：64 / 64



方法2，双向链表
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # index从0开始
    def get(self, index: int) -> int:
        # 无效index，直接返回-1
        if index < 0 or index >= self.size:
            return -1
        # 选择遍历数量少的一端开始遍历
        if (index + 1) < (self.size - index):
            curr_node = self.head
            for _ in range(index+1):
                curr_node = curr_node.next
            return curr_node.val
        else:
            curr_node = self.tail
            for _ in range(self.size - index):
                curr_node = curr_node.prev
            return curr_node.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        head_next = self.head.next
        new_node.next = head_next
        new_node.prev = self.head
        self.head.next = new_node
        head_next.prev = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        tail_prev = self.tail.prev
        new_node.next = self.tail
        new_node.prev = tail_prev
        tail_prev.next = new_node
        self.tail.prev = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # 如果index大于链表长度，则不会插入节点。
        if index > self.size:
            return
        # 如果index小于0，则在头部插入节点。
        if index < 0:
            return self.addAtHead(val)
        # 如果等于链表长度，则添加到链表的末尾
        elif index == self.size:
            return self.addAtTail(val)
        else:
            # 选择遍历数量少的一端开始遍历
            if (index + 1) < (self.size - index):
                curr_node = self.head
                for _ in range(index+1):
                    curr_node = curr_node.next
            else:
                curr_node = self.tail
                for _ in range(self.size - index):
                    curr_node = curr_node.prev
            prev_node = curr_node.prev
            new_node = ListNode(val)
            new_node.next = curr_node
            new_node.prev = prev_node
            prev_node.next = new_node
            curr_node.prev = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        # 如果index无效，则退出
        if index < 0 or index >= self.size:
            return
        # 如果index有效，则删除链表中的第index个节点
        # 选择遍历数量少的一端开始遍历
        if (index + 1) < (self.size - index):
            curr_node = self.head
            for _ in range(index+1):
                curr_node = curr_node.next
        else:
            curr_node = self.tail
            for _ in range(self.size - index):
                curr_node = curr_node.prev
        prev_node = curr_node.prev
        next_node = curr_node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1

执行用时：96 ms, 在所有 Python3 提交中击败了95.06%的用户
内存消耗：16.5 MB, 在所有 Python3 提交中击败了5.93%的用户
通过测试用例：64 / 64



