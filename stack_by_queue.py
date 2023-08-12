class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return self.top is None

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode
        self.n += 1

    def traversal(self):
        curr = self.top
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next

    def pop(self):
        if self.is_empty():
            return "Stack is underflowing"
        else:
            temp = self.top.data
            self.top = self.top.next
            self.n -= 1
            return temp

class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, value):
        self.s1.push(value)

    def dequeue(self):
        if self.s2.is_empty():
            if self.s1.is_empty():
                print("Queue is empty")
                return None
            else:
                # Lazy copying: Copy elements from s1 to s2 only when needed
                while not self.s1.is_empty():
                    self.s2.push(self.s1.pop())
        return self.s2.pop()

    def traversal(self):
        print("Queue elements:")
        self.s2.traversal()
        self.s1.traversal()
        print()

# Test the optimized queue implementation
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
 
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2

q.enqueue(6)
q.enqueue(7)

print(q.dequeue())  # Output: 3
print(q.dequeue())  # Output: 4

q.traversal()    # Output: 5 6 7
