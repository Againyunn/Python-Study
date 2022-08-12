class QUEUE():
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.isEmpty():
            return self.item.pop(0)
        
    def peek(self):
        if not self.isEmpmty():
            return self.items[-1]
    
    