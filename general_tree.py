# building general tree
class TreeNode:
    # each node have data, list of data, parent
    def __init__(self, data):
        self.data = data
        self.children = [] # list of object
        self.parent = None

    # get level of each node
    def get_level(self):
        level = 0 # root node level is 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    # print tree
    def print_tree(self):
        space = " " * self.get_level() * 4
        prefix = space + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for ch in self.children:
                ch.print_tree()

    # add node
    def addNode(self, child):
        child.parent = self
        self.children.append(child)

if __name__ == "__main__":

    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.addNode(TreeNode("Mac"))
    laptop.addNode(TreeNode("Surface"))
    laptop.addNode(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.addNode(TreeNode("iPhone"))
    cellphone.addNode(TreeNode("Google Pixel"))
    cellphone.addNode(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.addNode(TreeNode("Samsung"))
    tv.addNode(TreeNode("LG"))

    root.addNode(laptop)
    root.addNode(cellphone)
    root.addNode(tv)

    root.print_tree()


