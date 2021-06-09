'''
    Question - Use a single python list to implement 3 stacks.

    LOGIC-
    For stack 1 - [0],[1],[2] ->[0, n/3)
    For stack 2 - [3],[4],[6] ->[n/3, 2n/3)
    For stack 1 - [7],[8],[9] ->[2n/3, n)
'''
class MultiStack:
    def __init__(self, stacksize):
        self.numstacks= 3
        self.custlist= [0]*(stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize
    
    def isFull(self,stacknum):
        if self.sizes[stacknum] == self.stacksize:
            return True
        else:
            return False

    def isEmpty(self,stacknum):
        if self.sizes[stacknum] == 0:
            return True
        else:
            return False

    #helper function
    def indexOfTop(self,stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum]-1

    def push(self, item, stacknum):
        if self.isFull(stacknum):
            return "Stack full! Cannot insert any element."
        else:
            self.sizes[stacknum] += 1
            self.custlist[self.indexOfTop(stacknum)] = item
    
    def pop(self, stacknum):
        if self.isEmpty():
            return "Stack empty! No element to remove."
        else:
            value = self.custlist[self.indexOfTop(stacknum)]
            self.custlist[self.indexOfTop(stacknum)] = 0
            self.sizes[stacknum] -= 1
            return value

    def peek(self, stacknum):
        if self.isEmpty():
            return "Stack empty! No element to remove."
        else:
            value = self.custlist[self.indexOfTop(stacknum)]
            return value


customStack  = MultiStack(6)
print(customStack.isFull(0))
print(customStack.isEmpty(1))
customStack.push(1,0)
customStack.push(2,0)
customStack.push(3,2)
print(customStack.peek(1))
print(customStack.peek(0))
print(customStack.pop(0))

    

