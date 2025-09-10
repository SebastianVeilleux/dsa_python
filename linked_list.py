class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

def build_list(values):
    head = Node(values[0], None)
    prev = head
    for val in values:
        prev.next = Node(val, prev)
        prev = prev.next

    return head
