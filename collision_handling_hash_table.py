# implement hash table
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)] # in this array we store a list

    # get hash (get the index)
    def getHash(self, key):
        hash = 0
        for ch in key:
            hash += ord(ch)
        return hash % self.MAX

    # get item
    def __getitem__(self, key):
        idx = self.getHash(key)
        for kv in self.arr[idx]:
            if kv[0] == key:
                return kv[1]

    # set item
    def __setitem__(self, key, value):
        idx = self.getHash(key)
        found = False
        for i, kv in enumerate(self.arr[idx]):
            if kv[0] == key:
                found = True
                self.arr[idx][i] = (key, value)
        if not found:
            self.arr[idx].append((key, value))

    # delete item
    def __delitem__(self, key):
        idx = self.getHash(key)
        for i, kv in enumerate(self.arr[idx]):
            if kv[0] == key:
                del self.arr[idx][i]


if __name__ == "__main__":

    ht = HashTable()
    print(ht.getHash("March 6"))
    print(ht.getHash("March 17"))

    ht["March 6"] = 10
    ht["March 6"] = 20
    ht["March 6"] = 30
    ht["March 17"] = 17
    ht["March 17"] = 70
    print(ht["March 6"])
    print(ht["March 17"])

    print(ht.arr)
    del ht["March 6"]
    print(ht.arr)

    # del ht["March 17"]
    #
    # print(len(ht.arr))
    # print(ht.arr)
