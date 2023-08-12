class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def is_empty(self):
        return self.top == None
    
    def push(self,value):
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode

    def traversal(self):
        curr = self.top
        while curr != None:
            print(curr.data,end=" ")
            curr = curr.next
        print()

    def peek(self):
        if self.is_empty():
            return "Stack in underflowing"
        else:
            return self.top.data
    def pop(self):
        if self.is_empty():
            return "Stack in underflowing"
        else:
            temp = self.top.data
            self.top = self.top.next
            return temp 

def reversal(string):
    s = Stack()
    for i in string:
        s.push(i)
    result = ""
    while s.is_empty() !=  True:
        result += s.pop()
    print(result)

def text_editor(str1,str2):
    u = Stack()
    r = Stack()
    for i in str1:
        u.push(i)
    for i in str2:
        if i =='u' or i=="U":
            r.push(u.pop())
        elif i =='r' or i=="R":
            u.push(r.pop())
        else:
            print("Not allowed")
    res = ""
    while u.is_empty() != True:
        res = u.pop() + res
    return res

# s1 = Stack()
# s1.push(2)
# s1.push(3)
# s1.push(5)
# s1.push(8)
# s1.traversal()
# s1.pop()
# print(s1.peek())
# s1.pop()
# print(s1.peek())

reversal("HEllo")
print(text_editor("Hello","uru"))