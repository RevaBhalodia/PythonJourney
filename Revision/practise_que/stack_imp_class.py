class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print("Pushed:", item)

    def pop(self):
        if not self.is_empty():
            print("Popped:", self.stack.pop())
        else:
            print("Stack empty")

    def peek(self):
        if not self.is_empty():
            print("Top element:", self.stack[-1])

    def is_empty(self):
        return len(self.stack) == 0


s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.peek()
s.pop()
s.pop()