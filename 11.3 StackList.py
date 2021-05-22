'''
We will create a stack using a python list datatype, which doesn't have any pre-defined 
size-limit. 
'''

#create an empty list inside the stack class
class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

# time - complexity - O(1)
# space - complexity - O(1)

    #method 1 - isEmpty(), Time - O(1), Space-O(1)
    def isEmpty(self):
       if self.list == []:
           return True
       else:
           return False
    
    #method 2 - push(), Time - O(1 or n^2), Space-O(1)
    def push(self, value):
       self.list.append(value)
       return "The element has been successfully pushed into the stack."

    #method 3 - pop()-> returns and removes last element, Time - O(n), Space-O(1)
    def Pop(self):
        if self.isEmpty():
            return "No elements found in the stack."
        else:
            return self.list.pop()

    #method 4 - peek()-> returns last element, Time - O(1), Space-O(1)
    def Peek(self):
        if self.isEmpty():
            return "No elements found in the stack."
        else:
            return self.list[len(self.list)-1]

    #method 5 - delete()-> deleted entire stack from memory, Time - O(1), Space-O(1)
    def delete(self):
        self.list = None



''' Note - There is another additional method in stack called isFull() but we didn't create it here as we
are not using any size-limit, so we cannot check if the stack is full.
'''


#check methods. Create an object of stack class first 

customStack = Stack()
#print(customStack.isEmpty())
customStack.push(2)
customStack.push(7)
customStack.push(9)
customStack.push(3)
#print(customStack)
#print(customStack.Pop())
#print(customStack)
print(customStack.Peek())
print(customStack)


