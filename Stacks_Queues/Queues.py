class Queue:
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        return self.queue == []
    
    def enqueue(self,data):
        return self.queue.append(data)
    
    def dequeue(self):
        item = self.queue[0]
        del self.queue[0]
        return item
    
    def peek(self):
        return self.queue[0]
    
    def size(self):
        return len(self.queue)
    
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Dequeue: ",q.dequeue())
print(q.queue)