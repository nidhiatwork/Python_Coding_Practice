"""
    # Sum two numbers that are represented with linked lists with decimal digits
    # in reverse order of magnitude.
    
    num1 = Node(1,Node(2,Node(3)))
    num2 = Node(4,Node(9,Node(5)))
    self.assertEqual(str(sum_lists(num1, num2)), "5,1,9")
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def operate(a, b):
    runner = Node(0)
    head = runner
    carry = 0
    while a and b:
        s = a.val + b.val + carry
        carry = 1 if s>10 else 0
        n = Node(s%10)
        runner.next = n
        runner = runner.next
        a = a.next
        b = b.next
        if a and not b:
            n = Node(0)
            b = n
        elif b and not a:
            n = Node(0)
            a = n
    if carry:
        n = Node(carry)
        runner.next = n
    return head.next

# a = Node(9,Node(2,Node(3, Node(4, Node(1)))))
a = Node(1,Node(2,Node(3)))
b = Node(4,Node(9,Node(5)))

head = operate(a, b)
while head:
    print(head.val)
    head = head.next
