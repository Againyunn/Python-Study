from re import M
from tkinter.tix import MAX

global MAX_QSIZE
MAX_QSIZE = 10

class Circular_Queue():
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE
    
    def isEmtpy(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % MAX_QSIZE
    
    def clear(self):
        self.front = self.rear
    
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % MAX_QSIZE
            self.items[self.rear] = item
    
    def dequeue(self):
        if not self.isEmtpy():
            self.front = (self.front + 1) % MAX_QSIZE
            return self.items[self.front]
    
    def peek(self):
        if not self.isEmtpy():
            return self.items[(self.front + 1) % MAX_QSIZE]
    
    def size(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE
    
    def print_all(self):
        check = self.front + 1
        while check != (self.rear + 1) % MAX_QSIZE:
            print(self.items[check], end=" ")
            check = (check + 1) % MAX_QSIZE
        