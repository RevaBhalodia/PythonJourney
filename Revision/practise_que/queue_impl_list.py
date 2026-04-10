class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print("Inserted:", item)

    def dequeue(self):
        if self.queue:
            print("Removed:", self.queue.pop(0))
        else:
            print("Queue empty")

    def display(self):
        print(self.queue)


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

q.display()
q.dequeue()
q.display()