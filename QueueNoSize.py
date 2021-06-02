class Queue:

    def __init__(self):
        self.items = []

    def __str__(self): #time and space - O(1)
        
        values = [str(x) for x in self.items]

        return ' '.join(values)


    def isEmpty(self): #time and space - O(1)
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self,value): #time-O(n^2) and space - O(1)
        self.items.append(value)
        return "The element is inserted at the end of the queue."

    def dequeue(self): #time-O(n) and space - O(1)
        if self.isEmpty():
            return "No element found in the queue."
        
        else:
            return self.items.pop(0)

    def peek(self): #time-O(1) and space - O(1)
        if self.isEmpty():
            return "No element found in the queue."
        
        else:
            return self.items[0]

    def delete(self): #time-O(1) and space - O(1)

        self.items = None

customQueue = Queue()
#print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
print(customQueue.dequeue())
print(customQueue.peek())
print(customQueue)
customQueue.delete()
