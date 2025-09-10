class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

def build_list(values):
    head = Node(values[0], None)
    prev = head
    for val in values[1:]:
        prev.next = Node(val, None)
        prev = prev.next

    return head

def ll_to_list(head):
    data = []
    curr = head
    while curr != None:
        data.append(curr.data)
        curr = curr.next
    return data

def print_ll(head):
    curr = head
    counter = 0
    while curr != None:
        print(curr.data)
        counter += 1
        curr = curr.next
    
def insert_head(ll_head, data):
    new_head = Node(data,ll_head)
    
    return new_head
    

linked_list = build_list([1,2,3,4,5])
linked_list = insert_head(linked_list,0)
print_ll(linked_list)
