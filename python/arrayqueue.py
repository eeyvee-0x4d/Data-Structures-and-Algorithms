# Queues using circular array doesnt anymore require the shifting process when enqueueing and dequeueing elements
from array import Array

class Qeueue:
    def __init__(self, maxSize):
        self._count = 0
        self._front = 0
        self._back = maxSize - 1
        self._array = Array(maxSize)

    def isEmpty(self):
        return self._count == 0

    def isFull(self):
        return self._count == len(self._array)

    def __len__(self):
        return len(self._count)
    
    def enqueue(self, item):
        assert not self.isFull(), "Cannot enqueue to a full queue."

        maxSize = len(self._array)
        self._back = (self._back + 1) % maxSize
        self._array[self._back] = item
        self._count += 1

    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeque from an empty queue."

        item = self._array[self._front]
        maxSize = len(self._array)
        self._front = (self._front + 1) % maxSize
        self._count -= 1

        return item
