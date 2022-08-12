import my_circular_queue

Queue = my_circular_queue.Circular_Queue()

Queue.enqueue(5)
Queue.enqueue(6)
Queue.enqueue(7)
Queue.enqueue(8)
print(Queue.size())
Queue.print_all()