class Queue:
    
    def __init__(self, maxsize): # Time Complexity = O(1) Space Complexity = O(N)

        self.items = maxsize * [None]
        self.maxsize = maxsize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self): # Time Complexity = O(1) Space Complexity = O(1)
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxsize:
            return True 
        else:
            return False

    def isEmpty(self): # Time Complexity = O(1) Space Complexity = O(1)
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self,value):# Time Complexity = O(1) Space Complexity = O(1)
        if self.isFull():
            return "The queue is full, cannot insert element."
        else:
            if self.top + 1 == self.maxsize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of the queue."

    def dequeue(self):# Time Complexity = O(1) Space Complexity = O(1)
        if self.isEmpty():
            return "Queue is empty. Dequeue cannot be done in empty queue."
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxsize:
                self.start = 0
            else:
                self.start += 1

            self.items[start] = None
            return firstElement

    def peek(self):# Time Complexity = O(1) Space Complexity = O(1)
        if self.isEmpty():
            return "Queue is empty. Cannot perform peek in empty queue."
        else:
            return self.items[self.start]

    def delete(self):
        self.items = self.maxsize * [None]
        self.top = -1
        self.start = -1


customQueue = Queue(3)
#print(customQueue.isFull())
#print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(4)
print(customQueue.dequeue())
print(customQueue.peek())
    



