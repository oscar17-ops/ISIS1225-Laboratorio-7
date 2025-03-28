from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf

class MapLinearProbing:
    def __init__(self, capacity=11):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
        
        
    def new_map(self, capacity=11):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
        
    def put(self, key, value):
        index = mf.hash_function(key, self.capacity)
        original_index = index
        
        while self.table[index] is not None and self.table[index].key != key:
            index = (index + 1) % self.capacity
            if index == original_index:
                return
            
        if self.table[index] is None:
            self.size += 1
            
        self.table[index] = me.MapEntry(key, value)
        
    def contains(self, key):
        index = mf.hash_function(key, self.capacity)
        original_index = index
        
        while self.table[index] is not None:
            if self.table[index].key == key:
                return True
            index = (index + 1) % self.capacity
            if index == original_index:
                return False
            
        return False
    
    def get(self, key):
        index = mf.hash_function(key, self.capacity)
        original_index = index
        
        while self.table[index] is not None:
            if self.table[index].key == key:
                return self.table[index].value
            index = (index + 1) % self.capacity
            if index == original_index:
                return None
        
        return None
    
    def remove(self, key):
        index = mf.hash_function(key, self.capacity)
        original_index = index
        
        while self.table[index] is not None:
            if self.table[index].key == key:
               self.table[index] = None
               self.size -= 1
               return
            index = (index + 1) % self.capacity
            if index == original_index:
                return 
            
    def size(self):
        return self.size
        