# create hash table class
class Dictionary:
    # initialize constructor
    def __init__(self):
        self.MAX = 100
        self.arr = [None for _ in range(self.MAX)]

    # key in dictionary
    # this function get_hash(key) return index
    def get_hash(self, key):
        # we user ord() to convert string to asccii
        sum = 0
        for ch in key:
            sum += ord(ch)
        return sum % 100  # 100 is the number of element

    # add
    def add(self,key, value):
        index = self.get_hash(key)
        self.arr[index] = value # set the value to our array

    # get value from key
    def get(self, key):
        index = self.get_hash(key)
        return self.arr[index]

    # delete valuepp`
    def delete(self, key):
        index = self.get_hash(key)
        self.arr[index] = None

if __name__ == "__main__":
    # create instant of dictionary class
    dic = Dictionary()
    dic.add("march 6", 10) # our dictionary
    print(dic.get("march 6"))
    print("After delete: ", dic.delete("march 6"))