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
        print(e)
        if self.head==None: #head가 비어있을 때
            self.head=newNode
        else:
            currentNode=self.head
            while currentNode.link!=None:
                currentNode=currentNode.link
            currentNode.link=newNode.link
    
    def pop(self):
        if self.head==None:
            return print("LinkedList has no elements")
        else:
            currentNode=self.head
            while currentNode.link!=None:
                currentNode=currentNode.link
            return currentNode.data

#####수업시간의 내용####### (교수님 방식)
class LinkedList:
    def __init__(self):
        self.head=None
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

    def sizeRecursion(self, node):
        if node ==None:
            return 0
        else:
            return self.sizeRecur(node.link)+1
    
    def sizeRecur(self):
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

    def getEntry(self, pos):
        currentNode = self.getNode(pos) #getNode 메소드에 return 값이 currentNode.data가 아닌 이유
        if currentNode ==None:
            return None
        else:
            return currentNode.data
    
    def insert(self, pos, element):
        currentNode=Node(element)
        before = self.getNode(pos-1)
        if before == None: #기존에 저장된 Node가 없는 경우
            currentNode.link = self.head #self.head = Noen 상태인데, 어차피 첫번째 노드의 link는 비어있으므로 None 값을 저장
            self.head=currentNode #head에 새로운 Node의 값 추가
        else: #중간에 원소를 삽입할 경우
            currentNode.link=before.link #currentNode의 link에는 삽입할 Node의 다음 Node 주소 값 저장
            before.link=currentNode #삽입할 Node가 참조하고 있던 link를 추가할 Node의 link로 주소 값 저장

    def delete(self, pos):
        before= self.getNode(pos-1)
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

if __name__ == 'Main':
    print("start")
    L=LinkedList_JavaVersion()
    L.insert(1)
    L.insert('b')
    L.insert('c')
    answer=L.pop()
    print(answer)