# 우선순위 큐

class PriorityQueue:
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return len(self.items) ==0
    
    def size(self):
        return len(self.size)
    
    def claer(self):
        self.items=[]
    
    def enqueue(self, e):
        self.items.append(e) #리스트의 맨 뒤에 삽입
    
    def findMaxIndex(self):
        if self.isEmpty():
            return None
        else:
            highest = 0
            for i in range(1, self.size):
                if self.items[i]>self.items[highest]:
                    highest=i
            return highest
    
    def dequeue(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items.pop(highest)
        
    def peek(self):
        highest = findMaxIndex()
        if highest is not None:
            return self.items[highest]

