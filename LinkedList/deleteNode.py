'''
Delete a node from linked list if you only have access to that node only 
'''

class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def deleteNode(self, node):
        node.val=node.next.val
        node.next = node.next.next


root = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
node = root.next.next
root.deleteNode(node)
while root:
    print(root.val)
    root=root.next