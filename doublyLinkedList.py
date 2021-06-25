# Node class
class Node:
    # constructor
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

# Doubly Linked List Class
class DoublyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # insert
    def insert(self, data):
        node = Node(data, None, None)
        if self.head is None:
            self.head = node
            return
        else:
            itr = self.head
            while itr.next:
                itr = itr.next

            itr.next = node
            node.prev = itr

    # print
    def print(self):
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next
    # print backward
    def printBackward(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        while itr:
            print(itr.data)
            itr = itr.prev


    # get lenght
    def getLength(self):
        count = 0
        if self.head is None:
            return count
        else:
            itr = self.head
            while itr:
                count += 1
                itr = itr.next
            return count

    # insert at the beginning
    def insertAtBeginning(self, data):
        node = Node(data, None, None)
        if self.head is None:
            self.head = node
            return
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    # insert at index
    def insertAt(self, data, index):
        node = Node(data, None, None)
        if index == 0:
            self.insertAtBeginning(data)
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node.next = itr.next
                node.prev = itr
                itr.next = node
                break
            itr = itr.next
            count += 1

    # remove at
    def removeAt(self,index):
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                itr.next.next.prev = itr
            itr= itr.next
            count += 1

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert(10)
    dll.insert(20)
    dll.insert(30)
    dll.insert(40)
    dll.insert(50)
    dll.insert(60)
    # dll.insertAtBeginning(30)
    # dll.insertAtBeginning(40)
    # print("Old")
    # dll.print()
    # dll.insertAt(50, 2)
    # print("New")
    # dll.print()
    # print("After remove")
    # dll.removeAt(2)
    # dll.print()
    dll.printBackward()
    print(dll.getLength())
