from queue import PriorityQueue
from collections import defaultdict

myqueue = PriorityQueue()

myqueue.put((5, 'e'))
myqueue.put((6, 'f'))
myqueue.put((3, 'c'))
myqueue.put((7, 'g'))
myqueue.put((1, 'a'))
myqueue.put((2, 'b'))
myqueue.put((4, 'd'))

print(myqueue.queue)

myqueue.queue.sort(key = lambda x: x[0])
print(myqueue.queue)

# pop function

print(myqueue.get())
print(myqueue.queue)

# clear function

myqueue.queue.clear()
print(myqueue.queue)

