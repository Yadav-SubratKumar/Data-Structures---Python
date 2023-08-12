class Dictionary :
    def __init__(self,size):
        self.size = size
        self.slot = [None] * self.size
        self.data = [None] * self.size
        
    def rehash(self,old_hash):
        return (old_hash + 1) % self.size 

    def hash_function(self,key):
        return abs(hash(key)) % self.size

    def put(self,key,value):
        hash_value = self.hash_function(key)
        if self.slot[hash_value] == None:
            self.slot[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slot[hash_value] == key :
                self.data[hash_value] = value
            else :
                new_hash_value = self.rehash(hash_value)

                while self.slot[new_hash_value] != None and self.slot[new_hash_value] != key : 
                    new_hash_value = self.rehash(hash_value)

                if self.slot[new_hash_value] == None:
                    self.slot[new_hash_value] = key
                    self.data[new_hash_value] = value
                else:
                    self.data[new_hash_value] = value


    def __setitem__(self,key,value):
        self.put(key,value)


    def get(self,key) :
        start_position = self.hash_function(key)
        current_position = start_position

        while self.slot[current_position] != None:
            if self.slot[current_position] == key:
                return self.data[current_position]
            
            current_position = self.rehash(current_position)

            if current_position == start_position:
                return "Not Found"
            
        return "Not Present"

    def __getitem__(self,key):
        return self.get(key)

    def __str__(self):
        for i in range(len(self.slot)):
            if self.slot[i] != None:
                print(self.slot[i],":",self.data[i],end=" ")
        return ''

d1['s'] = 15
d1['y'] = 20
print(d1['s'])
print(d1)