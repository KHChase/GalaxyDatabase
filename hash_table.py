
class HashTable:
    def __init__(self):
        self.table = {}

    # insert into hash table
    def insert(self, key, value):
        if key not in self.table:
            self.table[key] = []

        self.table[key].append(value)

    # searching hash table
    def search(self, key):
        return self.table.get(key, None)
