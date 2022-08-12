import my_NODE

NODE = my_NODE.NODE()

class LinkedList():
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top == None
    
    def clear(self):
        self.top= None
    
    def push(self, item):
        node =  NODE(item, self.top)
        self.top = node
    

