import my_NODE

class LinkedList:
    node = None
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def clear(self):
        self.head= None
    
    def push(self, item):
        node = my_NODE.NODE(item, self.head)
        self.head = node
    
    def pop(self):
        if not self.isEmpty():
            node = self.head
            self.head = node.link
            return node.date
    
    def peek(self):
        if not self.isEmpty():
            return self.head.data
    
    def size(self):
        node = self.head
        count = 0

        while not node == None:
            node = node.link
            count += 1
        return count
    
    def display(self, msg ='LinkedStack'):
        print(msg, end=": ")
        node = self.head

        while not node == None:
            print(node.data, end=" ")
            node = node.link
        
        return

