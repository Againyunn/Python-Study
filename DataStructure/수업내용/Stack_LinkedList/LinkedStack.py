class Node:
    def __init__(self,e):
        self.data=e
        self.link=None

class LinkedStack: #top에 저장하고 top의 원소를 반환하는 방식
    def __init__(self):
        self.top=None
    def isEmpty(self):
        return self.top==None
    def push(self,e):
        newNode=Node(e)
        newNode.link=self.top
        self.top = newNode
    def pop(self,e):
        if(self.isEmpty()):
            print("Stack is empty")
            return
        else:
            e = self.top.data
            self.top = self.top.link
            return e

class LinkedListReverse: #마지막 Node에 저장하고 마지막 Node의 원소를 반환하는 방식
    def __init__(self):
        self.top=None
    def isEmpty(self):
        return self.top==None
    def push(self,e):
        newNode=Node(e)
        if self.top==None:
            self.top=newNode
            return
        else:
            currentNode=self.top
            while currentNode.link!=None:
                currentNode=currentNode.link
            currentNode.link=newNode
            return
    def pop(self):
        if self.top==None:
            return print("Stack is empty")
        else:
            currentNode=self.top
            while currentNode.link.link!=None:
                currentNode=currentNode.link    
            print(currentNode.link.data)
            currentNode.link=None
            return 
#직접 만들어본 LinkedListReverse 테스트 용
d=LinkedListReverse()
d.push(1)
d.push(2)
d.push(3)
d.pop()
d.pop()


    