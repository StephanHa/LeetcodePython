# 706 设计哈希映射
# https://leetcode.cn/problems/design-hashmap
#
# 不使用任何内建的哈希表库设计一个哈希映射（HashMap）。
# 实现 MyHashMap 类：
# MyHashMap() 用空映射初始化对象
# void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
# int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
# void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。
#
# 提示：
# 0 <= key, value <= 1000000

class MyHashMap:

    def __init__(self):
        self.bucket = 1009
        self.table = [[] for _ in range(self.bucket)]

    def hash(self, key):
        return key % self.bucket

    def put(self, key: int, value: int) -> None:
        hashkey = self.hash(key)
        for item in self.table[hashkey]:
            if item[0] == key:
                item[1] = value
                return
        self.table[hashkey].append([key, value])

    def get(self, key: int) -> int:
        hashkey = self.hash(key)
        for item in self.table[hashkey]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        for index, value in enumerate(self.table[hashkey]):
            if value[0] == key:
                self.table[hashkey].pop(index)
                break

# 执行用时：164 ms, 在所有 Python3 提交中击败了66.58%的用户
# 内存消耗：18.6 MB, 在所有 Python3 提交中击败了48.18%的用户
# 通过测试用例：36 / 36

