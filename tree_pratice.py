class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data <= self.data:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.add_child(data)
        else:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.add_child(data)
        
    def inorder(self):
        if self.left:
            self.left.inorder()
        if self.data!= None:
            print(self.data)
        if self.right:
            self.right.inorder()
    
    def preorder(self):
        if self.data!= None:
            print(self.data)
        if self.left:
            self.left.inorder()
    
        if self.right:
            self.right.inorder()
    
    def delval(self,value):
        if self.data == value:
            self.data= None
        
        if self.left:
            self.left.delval(value)
        
        if self.right:
            self.right.delval(value)
    
    def countNode(self):
        left_count = self.left.countNode() if self.left else 0
        right_count = self.right.countNode() if self.right else 0
        return left_count + right_count + (1 if self.data is not None else 0)
    
    def countleaves(self):
        if self.left is None and self.right is None:
            return 1 
        else: 
            left_leaves = self.left.countleaves() if self.left else 0
            right_leaves = self.right.countleaves() if self.right else 0
            return left_leaves + right_leaves
    
    def countNonLeaves(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is None or self.right is None: 
            return 1
        else :
            left_non_leaves = self.left.countNonLeaves() if self.left else 0
            right_non_leaves = self.right.countNonLeaves() if self.right else 0
            return left_non_leaves + right_non_leaves + (1 if self.data is not None else 0)
    
q1= TreeNode(10)
q1.add_child(15)
q1.add_child(13)
q1.add_child(20)
q1.add_child(17)
q1.add_child(8)
q1.add_child(5)
print()
q1.delval(10)
q1.delval(15)
q1.delval(13)

print(q1.countNode())
print()
print(q1.countleaves())

print(q1.countNonLeaves())