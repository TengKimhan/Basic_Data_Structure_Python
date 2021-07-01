# create a binary search tree class
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # add node to Binary Search Tree
    def add_child_node(self, data):
        if data == self.data:
            return # data already exist

        if data < self.data:
            if self.left:
                self.left.add_child_node(data)
            else:
                self.left = BinarySearchTreeNode(data) # put node(data) in the left

        if data > self.data:
            if self.right:
                self.right.add_child_node(data)
            else:
                self.right = BinarySearchTreeNode(data) # put node(data) in the right


    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data) # data here is the root of the tree

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child_node(elements[i])

    return root
if __name__ == "__main__":
    list = [15, 10, 20, 7, 12, 18, 21]
    bt = build_tree(list)
    print(bt.in_order_traversal())