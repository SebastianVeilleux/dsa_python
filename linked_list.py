class Node:
    def __init__(self, data, next = None):
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

def insert_tail(ll_head, data):
    curr = ll_head
    while curr.next != None:
        curr = curr.next
    
    curr.next = Node(data) 
    
def find(ll_head, value):
    curr = ll_head
    while curr != None:
        if(curr.data == value):
            return curr.data
        else:
            curr = curr.next
        
    return None

def delete_value (ll_head, value):
    if (ll_head and ll_head.data == value):
        return ll_head.next
        


linked_list = build_list([1,2,3,4,5])
delete_value(linked_list, 1)
print_ll(linked_list)
