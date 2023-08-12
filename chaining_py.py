class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LL:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.key, "-->", temp.value, end=" ")
            temp = temp.next
        print()

    def add(self, key, value):  # Accept key and value as arguments
        newNode = Node(key, value)  # Create a new node with key and value

        if not self.head:
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode
        self.n += 1

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head == None:
            print("Empty list")
        else:
            self.head = self.head.next
            self.n -= 1
        
    def remove(self, key):
        if not self.head:
            print("Empty list")
            return

        if self.head.key == key:
            self.head = self.head.next
            self.n -= 1
            return

        temp = self.head
        while temp.next:
            if temp.next.key == key:
                temp.next = temp.next.next
                self.n -= 1
                return
            temp = temp.next

        print("Not found")

    def search(self, key):
        temp = self.head
        pos = 0
        while temp:
            if temp.key == key:
                return pos
            temp = temp.next
            pos += 1
        return -1

    def get_node_at_index(self, index):
        temp = self.head
        pos = 0
        while temp:
            if pos == index:
                return temp
            temp = temp.next
            pos += 1
        return None


class Dictionary: 
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = self.make_array(self.capacity)

    def make_array(self, capacity):
        l = []
        for i in range(capacity):
            l.append(LL())
        return l

    def put(self, key, value):
        bucket_index = self.hash_function(key)
        node_index = self.get_node_index(bucket_index, key)
        if node_index == -1:
            # insert
            self.buckets[bucket_index].add(key, value)
            self.size += 1
            load_factor = self.size / self.capacity
            
            if (load_factor >= 2 ):
                self.rehash()
        else:
            node = self.buckets[bucket_index].get_node_at_index(node_index)
            node.value = value

    def __setitem__(self,key,value):
        self.put(key,value)

    def get(self,key):
        bucket_index = self.hash_function(key)
        res = self.buckets[bucket_index].search(key)
        if res == -1:
            return "Not found" 
        else:
            node =  self.buckets[bucket_index].get_node_at_index(res)
            return node.value

    def __getitem__(self,key):
        return self.get(key)

    def __delitem__(self,key):
        bucket_index = self.hash_function(key)
        self.buckets[bucket_index].remove(key)
        self.size -= 1
             
    def rehash(self ):
        self.capacity = self.capacity * 2
        old_buckets = self.buckets
        self.size = 0
        self.buckets = self.make_array(self.capacity)

        for i in old_buckets : 
            for j in range(i.size()) :
                node = i.get_node_at_index(j)
                key_item = node.key
                value_item = node.value
                self.put(key_item,value_item)

    def __str__(self):
        for i in self.buckets:
            i.traverse()
            return ""
    def __len__(self):
        return self.size
        
    def get_node_index(self, bucket_index, key):
        return self.buckets[bucket_index].search(key)

    def hash_function(self, key):
        return abs(hash(key)) % self.capacity

d1 = Dictionary(2)
d1["pypy"] =  34
d1["python"] =  134
del d1['pypy']
print(d1['pypy'])
print(d1)
print(len(d1))
