# Stack implementation using a python list
class ArrayStack:

    # instantiate the class
    def __init__(self):

        # create an empty stack
        self._data = []

    # returns the length of the stack
    def __len__(self):
        return len(self._data)

    # checks if the stack is empty
    # returns True if empty, returns False otherwise
    def isEmpty(self):
        return len(self._data) == 0

    # adds element into the stack
    def push(self, element):
        self._data.append(element)

    # returns the top element in the stack
    def top(self):

        # if stack in empty raise an error
        if self.isEmpty():
            raise Empty('Stack is Empty')

        return self._data[-1]

    # removes the top element from the stack
    def pop(self):
        
        # if stack is empty raise an error
        if self.isEmpty():
            raise Empty('Stack is Empty')

        return self._data.pop()

