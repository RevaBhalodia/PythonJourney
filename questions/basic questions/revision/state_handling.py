class Counter:
    def __init__(self):
        self.__count = 0 

    def increment(self):
        self.__count += 1  

    def decrement(self):
        if self.__count > 0:
            self.__count -= 1
        else:
            print("Count cannot go below 0")

    def reset(self):
        self.__count = 0

    def display(self):
        return self.__count

c = Counter()

c.increment()
c.increment()
print(c.display())  

c.decrement()
print(c.display())  

c.decrement()
c.decrement()   #dont go below 0

print(c.display())  

c.reset()
print(c.display())   
