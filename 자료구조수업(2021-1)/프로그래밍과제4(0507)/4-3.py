# N id를 입력하면 해당 학생의 id가 linkedlist에 반환
#       def 생성 insert함수

# C id를 입력하면 해당 학생의 id가 linkedlist에서 삭제
#       def 생성 delete함수

# S   를 입력하면 수강 학생 수를 출력
#       def 생성 size함수

# P   를 입력하면 학생들을 학번순서(오름차순)으로 출력
#       def 생성 print함수 + sort 오름차순 정렬 처리하여 출력(출력만 오름차순으로)

# Q   를 입력하면 메인함수의 반복을 끝냄
#       main def에서 처리

class Node:
    def __init__(self,e):
        self.data=e
        self.link = None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self, studentNum):
        newNode=Node(studentNum)
        if self.head == None: #기존에 저장된 Node가 없는 경우
            self.head =newNode 

        else: #중간에 원소를 삽입할 경우
            currentNode=self.head
            while currentNode.link!=None:
                currentNode=currentNode.link
            currentNode.link=newNode

    def delete(self, studentNum):
        if self.head == None:
            return
        currentNode=self.head

        if currentNode.link==None:
            self.head=None
            return

        else:
            while currentNode.link.link!=None:
                if currentNode.link.data == studentNum:
                    temp= currentNode.link.link
                    currentNode.link= temp
                    return
                currentNode = currentNode.link
            return

    def size(self):
        if self.head==None:
            return 0
        else:
            currentNode=self.head
            count=1
            while currentNode.link!=None:
                count+=1
                currentNode=currentNode.link
            return count

    def printAll(self):
        if self.head==None:
            return 0
        else:
            elements=[]
            currentNode=self.head
            while currentNode.link!=None:
                elements.append(currentNode.data)
                currentNode=currentNode.link
            elements.append(currentNode.data)
            elements.sort()
            return elements

L = LinkedList()   
while True:
    command = input().split()
    if command[0] == 'N':
        L.insert(command[1])
       # st_id(즉, command[1])를 수강자리스트에 insert: L.insert(command[1]) 
    elif command[0] == 'C':
        L.delete(command[1])
       # st_id(즉, command[1])를 수강자리스트에서 삭제: L.delete(command[1])
    elif command[0] == 'S':
        size=L.size()
        print(size)
       # 수강자리스트의 원소 수를 출력: L.size() 출력
    elif command[0] == 'P':
        if L.printAll() == 0:
            print("LinkedList doesn't have any elements")
        else:
            print(" ".join(L.printAll()))
       # 수강자리스트의 원소들을 오름차순으로 출력: L.print()
    elif command[0] == 'Q':
        break
    else:
        continue


    """
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

    def getEntry(self, pos):
        currentNode = self.getNode(pos) #getNode 메소드에 return 값이 currentNode.data가 아닌 이유
        if currentNode ==None:
            return None
        else:
            return currentNode.data
    """