class Node:
    def __init__(self,value):
        self.next = None
        self.value = value

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue (self,value):
        new_node = Node(value)

        if self.rear == None:
            self.front = new_node
            self.rear = self.front 
        else:
            self.rear.next = new_node
            self.rear = new_node  

    def dequeue (self):
        if self.front == None:
            return 'Empty'
        else:
            self.front = self.front.next
        
    def traverse(self):
        temp = self.front
        while temp != None:
            print(temp.value,end=" ")
            temp = temp.next
        print()

q1 = Queue()
q1.enqueue(-1)
q1.enqueue(0)
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.traverse()