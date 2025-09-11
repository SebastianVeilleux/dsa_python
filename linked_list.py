class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def build_list(values):
    if not values:
        return None
    head = Node(values[0], None)
    prev = head
    for val in values[1:]:
        prev.next = Node(val, None)
        prev = prev.next

    return head

def ll_to_list(head):
    data = []
    curr = head
    while curr:
        data.append(curr.data)
        curr = curr.next

    return data

def print_ll(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next
    
def insert_head(ll_head, data):
    new_head = Node(data,ll_head)

    return new_head

def insert_tail(ll_head, data):
    if not ll_head:
        return Node(data)
    curr = ll_head
    while curr.next:
        curr = curr.next
    curr.next = Node(data)

    return ll_head

    
def find(ll_head, value):
    curr = ll_head
    while curr:
        if(curr.data == value):
            return curr
        else:
            curr = curr.next
        
    return None

def delete_value (ll_head, value):

    if not ll_head:
        return None
    
    if ll_head.data == value:
        return ll_head.next

    
    prev = ll_head
    curr = ll_head.next

    while curr:
        if(curr.data == value):
            prev.next = curr.next
            return ll_head
        
        prev = curr
        curr = curr.next
    
    return ll_head

#            ---------------- Reverse Linked List LeetCode ----------------

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        return prev

'''

#           ---------------- Middle of Linked List ----------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
        
        if head.next is None:
            return head
            
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        return slow