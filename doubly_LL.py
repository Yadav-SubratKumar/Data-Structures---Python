class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        self.prev = None

class Doubly_LL:
    def __init__(self):
        self.head = None
        self.n = 0
        self.rear = None

    def __len__ (self):
        return self.n

    # Adding elments in the doubly linked list
    def insert_head(self,value):
        newNode = Node(value)
        if self.head == None:
            self.rear = newNode
        if self.head != None:
            self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode
        self.n +=1

    def append(self,value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.rear = newNode
        else:
            newNode.prev = self.rear
            self.rear.next = newNode
            self.rear = newNode
        self.n +=1

    # Printing elments in the doubly linked list

    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.data) + '<->'
            curr = curr.next
        return result[:-3] 
    
    def reverse_traverse(self):
        if self.rear == None:
            return None
        result = ''
        curr = self.rear
        while curr != None:
            result = result + str(curr.data) + '<->'
            curr = curr.prev
        return result[:-3]

    # Adding elments in the doubly linked list

    def delete_head(self):
        if self.head == None:
            print("Empty list")
        else:
            self.head = self.head.next
            self.n -= 1
        
    def pop(self):
        if self.head == None:
            print("Empty linked lists")
            return
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.n -= 1
    
    def remove(self,value):
        if self.head ==None:
            print("Empyt list")
            return
        if self.head.data == value:
            return self.delete_head()            
        
        curr = self.head
        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next

        if curr.next == None:
            print("Not found")
            return
        else:
            curr.next = curr.next.next 
        
l = Doubly_LL()
l.append(1)
l.append(0)
l.append(2)
l.append(3)
l.append(4)
# print(l)
# print(l.reverse_traverse())
l.pop()
print(l)
print(l.reverse_traverse())