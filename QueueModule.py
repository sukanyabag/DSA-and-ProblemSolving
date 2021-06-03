import queue as q

customQueue  = q.Queue(maxsize=3)
#print(customQueue.qsize())
print(customQueue.empty())
customQueue.put(1)
customQueue.put(3)
customQueue.put(8)
print(customQueue.qsize())
print(customQueue.full())
print(customQueue.get())
print(customQueue.qsize())