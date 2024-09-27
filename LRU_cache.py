class LRUCache:

    def __init__(self, capacity: int):
        self.c = 0
        self.size = capacity
        self.d = {}
        self.last_used = []
        

    def get(self, key: int) -> int:

        if key not in self.d:
            return -1

        self.last_used.remove(key)
        self.last_used.append(key)

        return self.d[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            # If key exists, update its value and move it to the end of the usage order
            self.d[key] = value
            self.last_used.remove(key)  # remove the key from its current position
            self.last_used.append(key)  # add it to the end as most recently used
        else:
            if self.c < self.size:
                # If cache is not full, simply add the new key-value pair
                self.c += 1
            else:
                # Cache is full, remove the least recently used item
                LRUkey = self.last_used.pop(0)  # remove the least recently used key
                del self.d[LRUkey]  # remove it from the cache

            # Add the new key-value pair and mark it as most recently used
            self.d[key] = value
            self.last_used.append(key)
