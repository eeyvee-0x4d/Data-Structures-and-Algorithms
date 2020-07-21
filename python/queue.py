# Queue - linear collection of items is which access is restricted to a first-in first-out basis. New items are inserted at the back and existing items are removed from the front.

class Queue:

    # initialize queue using list
    def __init__(self):
        self._queue = []

    # returns a boolean value indicating whether the queue is empty
    def isEmpty(self):
        return len(self._queue) == 0

    # returns the number of items currently in the queue
    def __len__(self):
        return len(self._queue)

    # adds the given item at the back of the queue
    def enqueue(self, value):
        self._queue.append(value)
    
    # removes and returns the value of the front of the queue. Cannot dequeue from an empty queue
    def dequeue(self):
        assert not self.isEmpty()

        return  self._queue.pop()
