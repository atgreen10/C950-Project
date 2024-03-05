#Self adjusting data structure

class HashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=41):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

# encodes the key using hash function
    def getHash(self, key):
        bucket = int(key) % len(self.table)
        return bucket

    # Inserts a new item into the hash table.
    def insert(self, key, value):
        # get the bucket list where this item will go.
        keyHash = self.getHash(key)
        keyValue = [key, value]

        if not self.table[keyHash]:
            self.table[keyHash] = list([keyValue])
            return True
        else:
            for pair in self.table[keyHash]:
                if pair[0] == key:
                    pair[1] = keyValue
                    return True
                else:
                    self.table[keyHash].append(keyValue)
                    return True

    # updates the saved key-value pair in the hash table.
    def update(self, key, value):
        keyHash = self.getHash(key)
        if self.table[keyHash] is not None:
            for pair in self.table[keyHash]:
                if pair[0] == int(key):
                    pair[1] = value
                    # print(pair[1])
                    return True
                else:
                    print("Error on update")

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def get(self, key):
        # get the bucket list where this key would be.
        keyHash = self.getHash(key)
        if self.table[keyHash] is not None:
            for pair in self.table[keyHash]:
                if pair[0] == key:
                    return pair[1]
            return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        keyHash = self.getHash(key)
        if self.table[keyHash] is None:
            return False
        for i in range(0, len(self.table[keyHash])):
            if self.table[keyHash][i][0] == key:
                self.table[keyHash].pop(i)
                return True
        return False

    def __iter__(self):
        self.num = 0
        return self

    # def __next__(self):
    #     if self.num >= self.max():
    #         raise StopIteration
    #     self.num += 1
    #     return self.num

