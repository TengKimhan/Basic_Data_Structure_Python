# creating a linked list

# 1. Create a node class
# node has data and pointer to next
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# create link list class
class LinkedList:
    def __init__(self):
        self.head = None # initialize head to null

    def insert(self, data):
        # create new node which contain data and next is null
        node = Node(data, None)
        # check if head is null
        if self.head is None:
            # take head as node that want to insert
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = node

    def printList(self):
        if self.head is None:
            print("Has no value")
            return

        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next

    def getLength(self):
        count = 1
        if self.head is None:
            return 0
        else:
            itr = self.head
            while itr.next:
                count = count + 1
                itr = itr.next
            return count

    def insertBeginning(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = node
            return
        else:
            node = Node(data, self.head)
            self.head = node

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        itr = self.head
        while itr:
            if itr.data == data_after:
                # Now insert data_to_insert after data_after node
                newNode = Node(data_to_insert, itr.next)
                itr.next = newNode
                break
            itr = itr.next

    def removeByIndex(self, index):
        if index == 0:
            self.head = self.head.next
            return
        else:
            count = 0;
            itr = self.head
            while itr:
                if count == index - 1:
                    itr.next = itr.next.next
                    break

                itr = itr.next
                count += 1

    def remove_by_value(self, data):
        # Remove first node that contains data
        itr = self.head
        idx = 0
        while itr:
            if itr.data == data:
                self.removeByIndex(idx)
                break
            itr = itr.next
            idx += 1

    def remove_by_value_another_version(self, data):
        itr = self.head
        if itr.data == data:
            itr.next = itr.next.next
            return

        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

if __name__ == "__main__":
    ll = LinkedList()
    # input
    while True:
        data = int(input("Enter number: "))
        if data == 0:
            break
        ll.insert(data)

    # ll.insertBeginning(70)
    ll.insert_after_value(3, 5)
    ll.printList()
    ll.remove_by_value_another_version(5)
    ll.printList()

