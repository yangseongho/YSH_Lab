class ArrayStack :
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity-1

    def push(self, e):
        if not self.isFull() :
            self.top += 1
            self.array[self.top] = e
        else : pass

    def pop(self):
        if not self.isEmpty():
            e = self.array[self.top]
            self.top -= 1
            return e
        return None

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        return None

    def __str__(self):
        return str([self.array[i] for i in range(self.top + 1)])

