class Node:
    def __init__(self, value=None):
        self.value = value
        self.next  = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next
class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

# tc and sc -O(1)

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False


# tc and sc -O(1)

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

# tc and sc -O(1)
    def Pop(self):
        if self.isEmpty():
            return "The stack is empty!"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue

# tc and sc -O(1)
    def peek(self):
        if self.isEmpty():
            return "The stack is empty!"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue


    def delete(self):
        self.LinkedList.head = None
        
customStack = Stack()
#print(customStack.isEmpty())
customStack.push(1)
customStack.push(4)
customStack.push(7)
print(customStack)
print('______________________')
customStack.Pop()
print(customStack)
print('______________________')
print(customStack.peek())
