class Node:
    def __init__(self, value=None):
        self.value = value 
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        currnode = self.head
        while currnode:
            yield currnode
            currnode = currnode.next

class Queue: # Time Complexity = O(1) Space Complexity = O(1)
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedlist]
        return ' '.join(values)

    def enqueue(self, value):# Time Complexity = O(1) Space Complexity = O(1)
        newNode = Node(value)
        if self.linkedlist.head == None:
            self.linkedlist.head = newNode
            self.linkedlist.tail = newNode
        else:
            self.linkedlist.tail.next = newNode
            self.linkedlist.tail = newNode

    def isEmpty(self):# Time Complexity = O(1) Space Complexity = O(1)
        if self.linkedlist.head == None:
            return True
        else:
            return False

    def dequeue(self):# Time Complexity = O(1) Space Complexity = O(1)
        if self.isEmpty():
            return "Cannot dequeue an element from an empty queue."
        else:
            tempNode = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            return tempNode

    def peek(self):# Time Complexity = O(1) Space Complexity = O(1)
        if self.isEmpty():
            return "Cannot peek from an empty queue."
        else:
            return self.linkedlist.head

    def delete(self): # Time Complexity = O(1) Space Complexity = O(1)
        self.linkedlist.head = None
        self.linkedlist.tail = None


customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(3)
customQueue.enqueue(8)
print(customQueue)
print(customQueue.dequeue())
print(customQueue)
print(customQueue.peek())

