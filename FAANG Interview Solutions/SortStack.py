'''Q- Sort a stack with the smallest element to the largest(at top) using only a single temporary stack.'''

# This function return the sorted stack
def sort_stack(stack):
  tempStack = createStack()
  while (isEmpty(stack) == False):
    temp = top(stack)
    pop(stack)

    # while temporary stack is not
        # empty and top of tempStack is
        # greater than temp
    while (isEmpty(tempStack)==False and int(top(tempStack))>int(temp)):
      push(stack, top(tempStack))
      pop(tempStack)

    push(tempStack,temp)
  
  return tempStack

# Function to create a stack. 
# It initializes size of stack
# as 0
def createStack():
  stack= []
  return stack

# Function to check if 
# the stack is empty
def isEmpty(stack):
  return len(stack) == 0

# Function to push an 
# item to stack
def push(stack,item):
  stack.append(item)

# Function to get top 
# item of stack
def top(stack):
  x = len(stack)
  return stack[x-1]

# Function to pop an 
# item from stack
def pop(stack):
  if isEmpty(stack):
    print("Stack Underflow")
    exit(1)
  else:
    stack.pop()

# Function to print the stack
def prints(stack):
  for i in range(len(stack)-1,-1,-1):
    print(stack[i], end=' ')
  print()

# Driver Code
stack = createStack()
push( stack, str(55) )
push( stack, str(4) )
push( stack, str(65) )
push( stack, str(78) )
push( stack, str(21) )
push( stack, str(69) )
  
print("Sorted numbers are: ")
sortedst = sort_stack( stack )
prints(sortedst)





