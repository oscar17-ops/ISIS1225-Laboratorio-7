from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf

class MapSeparateChaining:
    def __init__(self, capacity=11):
        """Inicializa la tabla de hash con una capacidad dada."""
        self.capacity = capacity
        self.size = 0
        self.table = [[] for _ in range(capacity)]  
    
    def new_map(self, capacity=11):
        """Crea una nueva tabla de hash con la capacidad especificada."""
        self.capacity = capacity
        self.size = 0
        self.table = [[] for _ in range(capacity)]
    
    def put(self, key, value):
        """Inserta un par llave-valor en la tabla de hash usando separate chaining."""
        index = mf.hash_function(key, self.capacity)
        bucket = self.table[index]
        
        for entry in bucket:
            if entry.key == key:
                entry.value = value  
                return
        
        bucket.append(me.MapEntry(key, value))
        self.size += 1
    
    def contains(self, key):
        """Verifica si una clave está en la tabla de hash."""
        index = mf.hash_function(key, self.capacity)
        bucket = self.table[index]
        
        return any(entry.key == key for entry in bucket)
    
    def get(self, key):
        """Obtiene el valor asociado a una clave en la tabla de hash."""
        index = mf.hash_function(key, self.capacity)
        bucket = self.table[index]
        
        for entry in bucket:
            if entry.key == key:
                return entry.value
        return None
    
    def remove(self, key):
        """Elimina una clave de la tabla de hash."""
        index = mf.hash_function(key, self.capacity)
        bucket = self.table[index]
        
        for i, entry in enumerate(bucket):
            if entry.key == key:
                del bucket[i]
                self.size -= 1
                return
    
    def get_size(self):
        """Retorna el tamaño actual de la tabla de hash."""
        return self.size
