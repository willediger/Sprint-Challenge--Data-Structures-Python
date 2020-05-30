class RingBuffer:
    def __init__(self, capacity):
        self.index = 0
        self.capacity = capacity
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def append(self, item):
        if len(self) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.index] = item

        if self.index ==  self.capacity - 1:
            self.index = 0
        else:
            self.index += 1

    def get(self):
        return self.storage