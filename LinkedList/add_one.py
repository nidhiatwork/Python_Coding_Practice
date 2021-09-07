'''
Delete a node from linked list if you only have access to that node only 
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def add_one(head,carry):  
    if not head.next:
        total = head.value+carry[0]
        head.value = total%10
        carry[0] = total//10
        return head
    head.next = add_one(head.next,carry)
    head.value = (head.value+carry[0])%10
    return head

root = Node(1, Node(2, Node(3)))
carry = [0]
root = add_one(root,carry)
while root:
    print(root.value)
    root=root.next