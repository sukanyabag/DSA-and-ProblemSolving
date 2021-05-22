'''
We will create a stack using a python list datatype, which has a pre-defined 
size-limit. 
'''
class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

# time - complexity - O(1)
# space - complexity - O(1)
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            return "The stack is full. Cannot push anymore elements."
        else:
            self.list.append(value)
            return "The element has been successfully pushed into the stack."

    def Pop(self):
        if self.isEmpty():
            return "No elements found in the stack."
        else:
            return self.list.pop()

    def Peek(self):
        if self.isEmpty():
            return "No elements found in the stack."
        else:
            return self.list[len(self.list)-1]

    def delete(self):
        self.list = None




customStack = Stack(5)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(2)
customStack.push(7)
customStack.push(9)
customStack.push(3)
print(customStack)
