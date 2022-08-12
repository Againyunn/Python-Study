class DummyNode:
    def __init__(self,e):
        self.data=e
        self.next=None

class DummyNodeLinkedList:
    def __init__ (self):
        self.length=0
        self.headData=self.length
        self.head=None
    
    def insert(self,e):
        newNode = DummyNode(e)

        if self.head ==None:
            self.head=newNode
            print("*",newNode.data)
        else:
            currentNode = self.head
            while currentNode.next != None:
                print("^")
                currentNode=currentNode.next
            currentNode.next=newNode.next
            print("**",newNode.data)
        self.length+=1
    
    def printAll(self):
        self.printRecur(self.head)

    def printRecur(self, currentNode):
        if currentNode != None:
            print(currentNode.data)
            self.printRecur(currentNode.next)
    
    def printAll1(self):
        node=self.head
        while node is not None:
            print(node.data)
            node=node.next

D=DummyNodeLinkedList()
D.insert(1)
D.insert(2)
D.printAll()
print("*")
D.insert(3)
D.printAll()
D.printAll1()