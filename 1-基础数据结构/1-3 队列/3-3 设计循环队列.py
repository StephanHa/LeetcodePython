622. 设计循环队列
https://leetcode.cn/problems/design-circular-queue/

设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。
循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

你的实现应该支持如下操作：
MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。

示例：
MyCircularQueue circularQueue = new MyCircularQueue(3); // 设置长度为 3
circularQueue.enQueue(1);  // 返回 true
circularQueue.enQueue(2);  // 返回 true
circularQueue.enQueue(3);  // 返回 true
circularQueue.enQueue(4);  // 返回 false，队列已满
circularQueue.Rear();  // 返回 3
circularQueue.isFull();  // 返回 true
circularQueue.deQueue();  // 返回 true
circularQueue.enQueue(4);  // 返回 true
circularQueue.Rear();  // 返回 4

提示：
1.所有的值都在 0 至 1000 的范围内；
2.操作数将在 1 至 1000 的范围内；
3.请不要使用内置的队列库。


方法1，单链表
复杂度分析
1. 时间复杂度：O(1)，所有方法都具有恒定的时间复杂度
2. 空间复杂度：O(n)，单链表存储元素的数量

class Node:
    def __init__(self, value: int, nextNode=None):
        self.value = value
        self.nextNode = None


class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.head = None
        self.tail = None
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            newNode = Node(value)
            self.tail.nextNode = newNode
            self.tail = newNode
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = self.head.nextNode
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.value

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.value

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity


执行用时：80 ms, 在所有 Python3 提交中击败了22.84%的
用户内存消耗：15.5 MB, 在所有 Python3 提交中击败了85.89%的用户
通过测试用例：58 / 58


方法2，列表
https://leetcode.cn/problems/design-circular-queue/solution/622she-ji-xun-huan-dui-lie-mian-shi-chan-yyis/


