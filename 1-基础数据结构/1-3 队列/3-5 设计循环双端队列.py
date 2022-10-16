641. 设计循环双端队列（中等）
https://leetcode.cn/problems/design-circular-deque

设计实现双端队列。
实现 MyCircularDeque 类:
MyCircularDeque(int k) ：构造函数,双端队列最大为 k 。
boolean insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true ，否则返回 false 。
boolean insertLast() ：将一个元素添加到双端队列尾部。如果操作成功返回 true ，否则返回 false 。
boolean deleteFront() ：从双端队列头部删除一个元素。 如果操作成功返回 true ，否则返回 false 。
boolean deleteLast() ：从双端队列尾部删除一个元素。如果操作成功返回 true ，否则返回 false 。
int getFront() ：从双端队列头部获得一个元素。如果双端队列为空，返回 -1 。
int getRear() ：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1 。
boolean isEmpty() ：若双端队列为空，则返回 true ，否则返回 false  。
boolean isFull() ：若双端队列满了，则返回 true ，否则返回 false 。

输入
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
输出
[null, true, true, true, false, 2, true, true, true, 4]
解释
MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
circularDeque.insertLast(1);       // 返回 true
circularDeque.insertLast(2);       // 返回 true
circularDeque.insertFront(3);      // 返回 true
circularDeque.insertFront(4);      // 已经满了，返回 false
circularDeque.getRear();           // 返回 2
circularDeque.isFull();            // 返回 true
circularDeque.deleteLast();        // 返回 true
circularDeque.insertFront(4);      // 返回 true
circularDeque.getFront();          // 返回 4

提示：
1 <= k <= 1000
0 <= value <= 1000
insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull  调用次数不大于 2000 次


方法1，数组
https://leetcode.cn/problems/design-circular-deque/solution/shu-zu-shi-xian-de-xun-huan-shuang-duan-dui-lie-by/
人为的浪费1个单位是为了保证“队列为空”与“队列为满”的判断条件不冲突：
1. 队列为空：front == rear （指向下一个可以存储数据的位置）
2. 队列为满：(rear+1)%capacity == front

class MyCircularDeque:
    def __init__(self, k: int):
        self.front = 0
        self.rear = 0
        self.capacity = k+1
        self.arr = [0 for _ in range(self.capacity)]

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        # 加上self.capacity是为避免减1后出现负值
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.arr[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr[self.rear] = value
        # self.rear指向下一个可以存储数据的位置
        self.rear = (self.rear + 1) % self.capacity
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[(self.rear - 1 + self.capacity) % self.capacity]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return (self.rear + 1) % self.capacity == self.front














