#데이터구조(java)식 LinkedList (내 방식)
class Node:
    def __init__(self,e):
        self.data=e
        self.link = None
    
class LinkedList_JavaVersion: #Stack형태
    def __init__(self):
        self.head=None

    def insert(self, e):
        newNode=Node(e)
        if self.head==None: #head가 비어있을 때
            self.head=newNode
        else:
            currentNode=self.head
            while currentNode.link!=None:
                currentNode=currentNode.link
            currentNode.link=newNode
    
    def pop(self):
        if self.head==None:
            return print("LinkedList has no elements")

        elif self.head.link == None:
            print(self.head.link.data)
            self.head=None

        else:
            currentNode=self.head
            while currentNode.link!=None:
                currentNode=currentNode.link
            print(currentNode.data)
            currentNode.data=None
            currentNode.link=None
    
    def printJava(self):
        if self.head == None:
            print("LinkedList has no elements")
        else:
            currentNode=self.head
            while currentNode.link!=None:
                print(currentNode.data)
                currentNode=currentNode.link
            print(currentNode.data)
            
               
            



####스택 형식의 단순연결리스트####
class LinkedStack:
    def __init__ (self):
        self.top = None
    
    def isEmpty(self):
        return self.top == None
    
    def push(self, e):
        newNode = Node(e)
        newNodd.link= self.top
        self.top = newNode
    
    def pop(self):
        if(self.isEmpty()):
            print("Stack is empty")
            return
        e = self.top.data
        self.top.data
        return e


####큐 형식의 단순연결리스트####
class LinkedQueue:
    def __init__ (self):
        self.front = self.rear = None
    
    def isEmpty(self):
        return self.front==None

    def enqueue(self):
        newNode= Node(e)
        if self.front == None:
            self.front = self.rear = newNode
            return
        else:
            self.rear.link=newNode
            self.rear= newNode

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        
        e= self.front.data
        self.front= self.front.link
        if self.front == None:
            self.rear = None
        
        return e

#####수업시간의 내용####### (교수님 방식)
class LinkedList:
    def __init__(self):
        self.head=None
        self.length=0

    def isEmpty(self):
        return self.head == None

    def clear(self):
        self.head = None

    def size(self):
        if self.head==None:
            return 0
        else:
            currentNode=head
            count=0
            while currentNode.link!=None:
                count+=1
                currentNode=currentNode.link
            return count

    def size2(self):
        return length

    def sizeRecursion(self, node): #재귀이용
        if node ==None:
            return 0
        else:
            return self.sizeRecursion(node.link)+1
    
    def sizeRecur(self): #재귀이용
        return self.sizeRecursion(self.head)

    def printAll(self):
        if self.head==None:
            return print("LinkedList doesn't have any elements.")
        else:
            currentNode=head
            while currentNode.link!=None:
                print(currentNode.data)
                if currentNode.link!=None:
                    print(", ")
                currentNode=currentNode.link
            return

    def getNode(self, pos): #getEntry 호출을 위한 Node 전체(link 와 data)를 불러오는 메소드
        if pos<0:
            return None
        currentNode = self.head
        while pos>0 and currentNode!=None:
            currentNode=currentNode.link
            pos-=1 #제어자 역할
        return currentNode

    def getNode2(self, pos):
        if pos<0:
            return None
        currentNode = self.head
        i =0
        for i in range(pos):
            if currentNode != None:
                currentNode=currentNode.link
        return currentNode



    def getNodeRecur(self, pos):
        return self.recurGetNode(self.head, pos)

    def recurGetNode(self, node, pos):
        if pos <0:
            return None
        elif pos ==0:    #pod = 0이면 node가 참조하는 노드를 반환
            return node
        else:
            return self.recurGetNode(node, pos-1)




    def getEntry(self, pos):
        currentNode = self.getNode(pos) #getNode 메소드에 return 값이 currentNode.data가 아닌 이유
        if currentNode ==None:
            return None
        else:
            return currentNode.data
    
    def insert(self, pos, element):
        currentNode=Node(element)
        before = self.getNode(pos-1)
        self.length+=1
        if before == None: #기존에 저장된 Node가 없는 경우
            currentNode.link = self.head #self.head = Noen 상태인데, 어차피 첫번째 노드의 link는 비어있으므로 None 값을 저장
            self.head=currentNode #head에 새로운 Node의 값 추가
        else: #중간에 원소를 삽입할 경우
            currentNode.link=before.link #currentNode의 link에는 삽입할 Node의 다음 Node 주소 값 저장
            before.link=currentNode #삽입할 Node가 참조하고 있던 link를 추가할 Node의 link로 주소 값 저장

    def delete(self, pos):
        before= self.getNode(pos-1)
        self.length-=1
        if before ==None:
            if self.head is not None:
                self.head= self.head.link
            elif before.link!=None:
                before.link=before.link.link
    
    def printAll(self):
        node=self.head
        while node is not None:
            print(node.data)
            node=node.link
    
    def printRecur(self, node):
        if node is not None:
            print(node.data)
            self.printRecur(node.link)
        
    def printAllRecur(self):
        self.printRecur(self.head)
    
    def length(self): # 내 방식의 원소 개수 측정
        currentNode=self.head
        count=0
        while currentNode.link!=None:
            count+=1
            currentNode=currentNode.link
        return count
    


#if __name__ == 'Main':
print("start")
L=LinkedList_JavaVersion()
#L=LinkedList()
L.insert(1)
L.insert('b')
L.insert('c')
#print(L.getNode(1))
#print(L.getNode2(1))
#print(L.sizeRecur())
L.printJava()
L.pop()
L.pop()
#answer=L.delete(2)
#print(answer)
#print(answer2)
#length=L.length()
#print(f"연결리스트의 원소 개수 : {length}")