class ArrayList:
    def __init__(self, initial_capacity=10):
        """Inicializa la lista con una capacidad inicial."""
        self.capacity = initial_capacity
        self.size = 0
        self.array = [None] * initial_capacity

    def _resize(self, new_capacity):
        """Redimensiona la lista cuando alcanza su capacidad máxima."""
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def add(self, item):
        """Añade un elemento al final de la lista."""
        if self.size == self.capacity:
            self._resize(self.capacity * 2)  # Duplicar capacidad si está llena
        self.array[self.size] = item
        self.size += 1

    def insert(self, index, item):
        """Inserta un elemento en un índice específico."""
        if index < 0 or index > self.size:
            raise IndexError("Índice fuera de rango")
        
        if self.size == self.capacity:
            self._resize(self.capacity * 2)

        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]

        self.array[index] = item
        self.size += 1

    def get(self, index):
        """Obtiene el elemento en un índice dado."""
        if index < 0 or index >= self.size:
            raise IndexError("Índice fuera de rango")
        return self.array[index]

    def remove(self, index):
        """Elimina un elemento en un índice específico y ajusta la lista."""
        if index < 0 or index >= self.size:
            raise IndexError("Índice fuera de rango")

        removed_item = self.array[index]

        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.size - 1] = None  # Limpiar la referencia
        self.size -= 1

        return removed_item

    def contains(self, item):
        """Verifica si un elemento está en la lista."""
        for i in range(self.size):
            if self.array[i] == item:
                return True
        return False

    def index_of(self, item):
        """Devuelve el índice de un elemento o -1 si no está en la lista."""
        for i in range(self.size):
            if self.array[i] == item:
                return i
        return -1

    def is_empty(self):
        """Verifica si la lista está vacía."""
        return self.size == 0

    def get_size(self):
        """Retorna el tamaño actual de la lista."""
        return self.size

    def clear(self):
        """Limpia todos los elementos de la lista."""
        self.array = [None] * self.capacity
        self.size = 0

    def __iter__(self):
        """Permite iterar sobre la lista."""
        for i in range(self.size):
            yield self.array[i]

    def __repr__(self):
        """Representación en string de la lista."""
        return "[" + ", ".join(str(self.array[i]) for i in range(self.size)) + "]"