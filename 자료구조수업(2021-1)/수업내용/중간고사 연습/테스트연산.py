from Queue import *

values= Queue()
for i in range(20):
    if i%3 ==0:
        values.enqueue(i)

print(Queue.qsize)
