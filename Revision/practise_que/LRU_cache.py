class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.order = []
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) == self.capacity:
            oldest = self.order.pop(0)
            del self.cache[oldest]

        self.cache[key] = value
        self.order.append(key)


lru = LRUCache(2)

lru.put(1, 10)
lru.put(2, 20)
print(lru.get(1))  # 10
lru.put(3, 30)     # removes key 2
print(lru.get(2))  # -1