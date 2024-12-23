class Stack:
    def __init__(self):
        # Inicializa una lista vacía para la pila
        self.stack = []

    # Verifica si la pila está vacía
    def is_empty(self):
        return len(self.stack) == 0

    # Agrega un elemento al tope de la pila
    def push(self, value):
        self.stack.append(value)

    # Elimina y devuelve el elemento en el tope de la pila
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("La pila está vacía. No se puede hacer pop.")

    # Devuelve el elemento en el tope de la pila sin eliminarlo
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("La pila está vacía. No se puede hacer peek.")

    # Devuelve el tamaño de la pila
    def size(self):
        return len(self.stack)

    # Muestra todos los elementos de la pila (para depuración)
    def display(self):
        print(self.stack)


# Crear una instancia de Stack
my_stack = Stack()

# Añadir elementos
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

# Mostrar la pila
my_stack.display()  # Salida: [10, 20, 30]

# Obtener el tamaño
print("Tamaño:", my_stack.size())  # Salida: 3

# Ver el tope sin eliminarlo
print("Tope:", my_stack.peek())  # Salida: 30

# Eliminar el tope
print("Pop:", my_stack.pop())  # Salida: 30

# Mostrar la pila después de hacer pop
my_stack.display()  # Salida: [10, 20]