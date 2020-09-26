class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = []
        self.current_removal = 0

    def append(self, item):
        if len(self.list) < self.capacity:
            self.list.append(item)
        elif len(self.list) == self.capacity:
            self.list.pop(self.current_removal)
            self.list.insert(self.current_removal, item)
            if self.current_removal < self.capacity - 1:
                self.current_removal += 1
            else:
                self.current_removal =  0

    def get(self):
        return self.list