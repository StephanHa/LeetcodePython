# 1019. 链表中的下一个更大节点（中等）
# 给定一个长度为n的链表head
# 对于列表中的每个节点，查找下一个更大节点的值。也就是说，对于每个节点，找到它旁边的第一个节点的值，这个节点的值严格大于它的值。
# 返回一个整数数组 answer ，其中 answer[i] 是第 i 个节点( 从1开始 )的下一个更大的节点的值。
# 如果第 i 个节点没有下一个更大的节点，设置answer[i] = 0。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/next-greater-node-in-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 方法1，单调递减栈+遍历链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        node = head
        stack = list()  # (val, index)
        temp = dict()
        index = 0
        while node:
            while stack and stack[-1][0] < node.val:
                # 哈希表以索引为key，节点值为value
                temp[stack.pop()[1]] = node.val
            stack.append((node.val, index))
            node = node.next
            index += 1
        # 链表节点数为index，生成结果数组，初始值为0，默认未找到下个值更大的节点
        result = [0 for _ in range(index)]
        for i in range(index):
            if i in temp.keys():
                result[i] = temp[i]
            else:
                result[i] = 0
        return result

# 执行用时：216 ms, 在所有 Python3 提交中击败了42.06%的用户
# 内存消耗：20.7 MB, 在所有 Python3 提交中击败了5.56%的用户
# 通过测试用例：76 / 76

# 优化
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        node = head
        stack = list()  # (val, index)
        temp = dict()
        index = 0
        while node:
            while stack and stack[-1][0] < node.val:
                # 哈希表以索引为key，节点值为value
                temp[stack.pop()[1]] = node.val
            stack.append((node.val, index))
            node = node.next
            index += 1
        # 链表节点数为index，生成结果数组，初始值为0，默认未找到下个值更大的节点
        result = [0 for _ in range(index)]
        for i in temp.keys():
            result[i] = temp[i]
        return result

# 执行用时：256 ms, 在所有 Python3 提交中击败了10.71%的用户
# 内存消耗：20.5 MB, 在所有 Python3 提交中击败了10.32%的用户
# 通过测试用例：76 / 76


# 方法2，链表转数组+单调递减栈
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        node = head
        nums = list()
        # 将链表转成数组
        while node:
            nums.append(node.val)
            node = node.next
        # 单调递减栈
        stack = list() # index 记录数组的元素下标
        n = len(nums)
        result = [0 for _ in range(n)]
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                # 栈顶元素值小，则出栈，结果数组的相应位置，记录为当前数组遍历的值
                result[stack.pop()] = nums[i]
            stack.append(i)
        return result

# 执行用时：184 ms, 在所有 Python3 提交中击败了97.22%的用户
# 内存消耗：19.1 MB, 在所有 Python3 提交中击败了92.86%的用户
# 通过测试用例：76 / 76

