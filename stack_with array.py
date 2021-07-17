# create stack with array
# import maxsize from sys module
# Used to return -infinite when stack is empty
from sys import maxsize

class Stack:
    def __init__(self):
        self.stack = []
        self.len = len(self.stack)

    # check if empty
    def isEmpty(self):
        return len(self.stack) == 0

    # push key in stack:
    def push_key(self, item):
        self.stack.append(item)

    # pop key in stack:
    def pop_key(self):
        if self.isEmpty():
            return str(-maxsize - 1)
        return self.stack.pop()

    def top(self):
        if self.isEmpty():
            return str(-maxsize - 1)
        return self.stack[len(self.stack)-1]

    def print(self):
        print(self.stack)

if __name__ == "__main__":
    # Driver program to test above functions
    st = Stack()
    st.push_key(10)
    st.push_key(20)
    st.print()
