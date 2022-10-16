class MyHashSet:

    def __init__(self):
        self.bucket = 1009
        self.tables = [[] for _ in range(self.bucket)]

    def hash(self, key):
        return key % self.bucket

    def add(self, key: int) -> None:
        hashkey = self.hash(key)
        if key not in self.tables[hashkey]:
            self.tables[hashkey].append(key)
            
    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        if key in self.tables[hashkey]:
            self.tables[hashkey].remove(key)

    def contains(self, key: int) -> bool:
        hashkey = self.hash(key)
        if key in self.tables[hashkey]:
            return True
        else:
            return False