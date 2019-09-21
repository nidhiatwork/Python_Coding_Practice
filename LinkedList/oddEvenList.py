''''''
class ListNode:
        def __init__(self, val, next=None):
                self.val = val
                self.next = next

def oddEvenList(head):  
        if not head: 
                return
        odd = head
        even = head.next
        dummy_even = even
        while even and even.next:
                odd.next = even.next
                odd = odd.next
                even.next = odd.next
                even = even.next
        odd.next = dummy_even
        return head


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
head = oddEvenList(head)
while head:
        print(head.val)
        head = head.next