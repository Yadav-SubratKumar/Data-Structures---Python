class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
        self.n = 0
        
    def __len__(self):
        return self.n

    def insert_head(self,value):
        newNode = Node(value)

        newNode.next = self.head
        self.head = newNode
        self.n += 1

    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]

    def append(self,value):
        newNode = Node(value)
        curr = self.head 
        while curr.next != None:
            curr = curr.next
        curr.next = newNode
        self.n +=1

    def insert_middle(self,after,value):
        newNode = Node(value)
        curr = self.head
        while curr != None:
            if curr.data == after:
                break
            curr = curr.next
        if curr != None:
            newNode.next = curr.next
            curr.next = newNode
            self.n += 1
        else:
            print("Item not Found")

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head == None:
            print("Empty list")
        else:
            self.head = self.head.next
            self.n -= 1
        
    def pop(self):
        curr = self.head
        if curr == None:
            print("Empty linked lists")
            return
        if curr.next == None:
            return self.delete_head()

        while curr.next.next != None:
            curr = curr.next
        
        curr.next != None
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
        
    def search(self,item):
        curr = self.head
        pos = 0 
        while curr != None:
            if curr.data== item:
                return pos
            curr = curr.next
            pos += 1
        return "Not Found"
    def __getitem__(self,index):
        curr = self.head
        pos = 0 
        while curr != None:
            if pos == index:
                return curr.data 
            curr = curr.next
            pos +=1
        return "Index Error"

    def del_Index(self,index):
        curr = self.head
        pos = 0 
        if curr is None:
            return
        if index == 0:
            self.head = curr.next
            return
        while curr.next is not None and pos < index - 1:
            curr = curr.next
            pos += 1
        if curr.next is None:
            print("Error: Index out of range")
            return
        curr.next = curr.next.next


        
    ''' Extra function for pratice   '''
    def replace_max(self,value):
        curr = self.head
        temp = self.head
        while curr != None:
            if temp.data < curr.data:
                temp = curr
            curr = curr.next
        temp.data = value
    
    def odd_Sum(self):
        total = 0
        pos = 0
        curr = self.head
        while curr != None:
            if pos % 2 != 0:
                total += curr.data
            pos +=1
            curr = curr.next
        return total

    def reversal(self):
        prev_node = None
        curr = self.head
        while curr != None:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node
l = linkedList()
l.insert_head(1)
l.insert_head(2)
l.insert_head(3)
l.insert_head(4)
l.insert_head(5)
l.insert_head(6)
l.insert_head(7)
l.insert_head(8)
l.insert_head(9)
# l.append('a')
# # l.insert_middle(1,45)
# # l.delete_head()
# # l.remove(3)
# # print(l.search(5))
# # l.del_Index(2)
# print(l[6])
# l.replace_max(15)
print(l)
l.reversal()
print(l)


