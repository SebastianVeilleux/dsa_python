from collections import deque

class Queue:
    def __init__(self):
        # Inicializa una cola vacía usando deque
        self.queue = deque()

    # Verifica si la cola está vacía
    def is_empty(self):
        return len(self.queue) == 0

    # Agrega un elemento al final de la cola
    def enqueue(self, value):
        self.queue.append(value)

    # Elimina y devuelve el primer elemento de la cola (FIFO)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()  # O(1) en lugar de O(n)
        else:
            raise IndexError("La cola está vacía. No se puede hacer dequeue.")

    # Devuelve el primer elemento de la cola sin eliminarlo
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("La cola está vacía. No se puede ver el frente.")

    # Devuelve el último elemento de la cola sin eliminarlo
    def rear(self):
        if not self.is_empty():
            return self.queue[-1]
        else:
            raise IndexError("La cola está vacía. No se puede ver el final.")

    # Devuelve el tamaño de la cola
    def size(self):
        return len(self.queue)

    # Muestra todos los elementos de la cola (para depuración)
    def display(self):
        print(list(self.queue))  # Convierte deque en lista para mostrarla


# Crear una instancia de Queue
my_queue = Queue()

# Añadir elementos
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

# Mostrar la cola
my_queue.display()  # Salida: [10, 20, 30]

# Obtener el tamaño
print("Tamaño:", my_queue.size())  # Salida: 3

# Ver el primer y último elemento
print("Frente:", my_queue.front())  # Salida: 10
print("Final:", my_queue.rear())    # Salida: 30

# Eliminar el primer elemento
print("Dequeue:", my_queue.dequeue())  # Salida: 10

# Mostrar la cola después de hacer dequeue
my_queue.display()  # Salida: [20, 30]