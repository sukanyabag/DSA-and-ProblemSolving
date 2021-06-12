'''Q4 -  Implement a queue using two stacks. Logic- Make two stacks. on stack1 enqueue elements,
then dequeue all elements to stack2, and the elements now gets stored in stack2 in reverse order.
So, now we can use pop() method to pop out the first element. After 1st element is popped,
we put back the rest elements in stack 1 again.'''

class Stack():
  def __init__(self):
    self.list = []

  def __len__(self):
    return len(self.list)

  def push(self,item):
    self.list.append(item)

  def pop(self):
    if len(self.list) == 0:
      return None
    return self.list.pop()

class QueueViaStack():
    def __init__(self):
      self.inStack = Stack()
      self.outStack = Stack()
    
    def enqueue(self,item):
      self.inStack.push(item)

    def dequeue(self):
      while len(self.inStack):
        self.outStack.push(self.inStack.pop())

      result = self.outStack.pop()

      while len(self.outStack):
        self.inStack.push(self.outStack.pop())

      return result


customQueue = QueueViaStack()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.dequeue())
