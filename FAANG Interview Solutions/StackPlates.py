'''
Q3. STACK OF PLATES
'''

class PlateStack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        return self.stacks

    def push(self,item):
        if len(self.stacks) > 0 and (len(self.stacks[-1]) < self.capacity):
            self.stacks[-1].append(item)

        else:
            self.stacks.append([item]) # since we have 2D lists in our case 1 stack-> one list and so on 

    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0 :
            self.stacks.pop()
            if len(self.stacks)==0:
                return None
            else:
                self.stacks[-1].pop()

    def popAt(self, stacknumber):
        if len(self.stacks[stacknumber]) > 0:
            return self.stacks[stacknumber].pop()
        else:
            return None

customStack = PlateStack(2)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack.popAt(0))




