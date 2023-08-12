class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        if isinstance(child, TreeNode):
            child.parent = self
            self.children.append(child)
        else:
            raise TypeError("Child should be a TreeNode object.")

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

ceo = TreeNode("Nilupul (CEO)")
cto = TreeNode("Chinmay (CTO)")
hr = TreeNode("Gels (HR Head)")
ih = TreeNode("Vishwas (Infrastructure Head)")

ceo.add_child(cto)
ceo.add_child(hr)
cto.add_child(ih)
ih.add_child(TreeNode("Dhaval (Cloud Manager)"))
ih.add_child(TreeNode("Abhijit (App Manager)"))

cto.add_child(TreeNode("Aamir (Application Head)"))
hr.add_child(TreeNode("Peter (Recruitment Manager)"))
hr.add_child(TreeNode("Wapas (Recruitment Manager)"))

ceo.print_tree()
