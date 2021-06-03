from collections import deque

customQueue = deque(maxlen=3)
print(customQueue)

customQueue.append(2)
customQueue.append(4)
customQueue.append(6)
customQueue.append(9) #overrides 1st element if maxlen is specified
print(customQueue)
print(customQueue.popleft())
print(customQueue)
print(customQueue.clear())
print(customQueue)