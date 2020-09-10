class Node(object):
      def __init__(self, val, next=None):
            self.val = val
            self.next = next

def removeNodes(head):
      runner = head
      while runner.next is not head:
            runner.next = runner.next.next
            runner = runner.next
            if runner==head:
                  break
      return head

head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(3))))))
head.next.next.next.next.next.next = head
head = removeNodes(head)
i=1
while i<=10:
    print(head.val)
    head = head.next
    i+=1