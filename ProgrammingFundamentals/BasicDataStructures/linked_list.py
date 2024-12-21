# Define a class representing a node in the linked list
class Node:
    # Constructor to initialize the node with data and an optional next node
    def __init__(self, data = None, next = None):
        self.data = data  # The data the node will hold
        self.next = next  # The pointer to the next node (default is None)

# Define a class for the LinkedList
class LinkedList:
    # Constructor to initialize an empty linked list
    def __init__(self):
        self.head = None  # The head points to the first node in the list (initially None)
        
    # Method to insert a new node at the beginning of the list
    def insert_at_beginning(self, data):
        node = Node(data, self.head)  # Create a new node, pointing to the current head
        self.head = node  # Make the new node the head of the list
        
    # Method to print all nodes in the linked list
    def print(self):
        current = self.head  # Start from the head of the list
        # Loop through the list, printing each node's data
        while(current != None):
            print(current.data)  # Print the data of the current node
            current = current.next  # Move to the next node in the list
    
    # Method to insert a new node at the end of the list
    def insert_at_end(self, data):
        current = self.head  # Start from the head of the list
        
        # Traverse the list to find the last node
        while current.next is not None:
            current = current.next
        
        # Create a new node with the provided data and link it to the last node
        current.next = Node(data)
        
    # Method to insert multiple values into the linked list
    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)  # For each value in the list, insert it at the end
        
    # Method to remove a node at a specific index
    def remove_at(self, index):
        # Ensure the index is non-negative
        if index < 0:
            raise IndexError("Index cannot be negative")
        
        # Raise an error if the list is empty
        if self.head == None:
            raise IndexError("List is empty")
        
        # Special case: if the index is 0, remove the head node
        if index == 0:
            self.head = self.head.next
        else:
            prev = None
            current = self.head
            # Traverse the list to find the node at the given index
            for i in range(index):
                prev = current
                current = current.next
                # Raise an error if the index is out of bounds
                if current is None:
                    raise IndexError("Index out of bounds.")
                
            prev.next = current.next  # Skip the node to remove it
            
    # Method to insert a node at a specific index
    def insert_at(self, index, data):
        # Ensure the index is non-negative
        if index < 0:
            raise IndexError("Index cannot be negative")
        
        # Special case: insert at the beginning if index is 0
        if self.head and index == 0:
            self.head = Node(data)  # Create a new node and set it as the head
            return
        
        prev = None
        current = self.head
        # Traverse the list to find the node just before the given index
        for i in range(index):
            prev = current
            current = current.next
            # Raise an error if the index is out of bounds
            if current is None:
                raise IndexError("Index out of bounds")

        # Create a new node with the provided data
        newNode = Node(data)
        prev.next = newNode  # Link the previous node to the new node
        newNode.next = current  # Link the new node to the next node
    
# Main function to run the program
if __name__ == '__main__':
    print("Hola Mundo")  # Print "Hola Mundo" to the console
