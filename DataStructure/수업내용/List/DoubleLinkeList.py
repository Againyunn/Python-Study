class DNode:
    def __init__ (self, e):
        self.data= e
        self.back= None
        self.next= None
    
class DoubleLinkedList:
    def __init__(self):
        head= None

    def insert(self, pos, e):
        newNode=DNode(e)
        currentNode=self.head   
        count=0
        while(currentNode.next!=None):
            count+=1
            if(count==pos):
                break
            currentNode=currentNode.next
        location=currentNode

        newNode.back= location.back   #newNode를 location Node 바로 앞에 삽입하겠다는 의미
        newNode.next=location

        if(location.back== None):
            head = newNode
        else:
            location.back.next = newNode
        loction.back = newNode

    def delete(self, pos, e):
        newNode=DNode(e)
        currentNode=self.head
        count=0
        while(currentNode.next!=None):
            count+=1
            if(count==pos):
                break
            currentNode=currentNode.next
        location=currentNode

        if(location.back == None):
            head = location.next
            if(location != None):
                location.next.back=None
        else:
            location.back.next = location.next
            if(location.next != None):
                location.next.back = location.back
                


        


