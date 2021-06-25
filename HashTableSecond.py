# use python descriptor
class Dictionary:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for _ in range(self.MAX)]

    # hash function which is the function that convert key string to index
    def get_hash(self,key):
        sum = 0
        for ch in key:
            sum += ord(ch) # ord() convert character to ascii
        return sum % self.MAX

    # add the value
    def __setitem__(self, key, value):
        index = self.get_hash(key)
        self.arr[index] = value

    # get the value by the key
    def __getitem__(self, key):
        index = self.get_hash(key)
        return self.arr[index]

    # delete the value
    def __delitem__(self, key):
        index = self.get_hash(key)
        self.arr = None

if __name__ == "__main__":
    dic = Dictionary()
    # add the value
    dic["Kimhan"] = 21
    dic["Huyly"]  = 21

    # get the value from key
    print("Kimhan value: ", dic["Kimhan"])
    print("Huyly  value: ", dic["Huyly"])

    # delete by the key
    del dic["Kimhan"]

    # result
    print("Final Result: ", dic)
