stockBook =[]
saledBook =[]

class Node:
    def __init__ (self, bookNum, bookName = None, price = None, num = None, left = None, right = None):
        self.bookNum = bookNum #key
        self.bookName = bookName
        self.price = price
        self.num = num
        self.left = None
        self.right = None

class saledNode: #판매된 도서 데이터를 담아두는 트리
    def __init__ (self, bookNum, bookName = None, price = None, num = None):
        self.bookNum = bookNum
        self.bookName = bookName
        self.price = price
        self.num = num

class BST:
    def __init__ (self):
        self.root = None
        self.rootSaled = None
    
    #신규등록 연산
    def insert(self, bookNum, bookName, price, num):
        self.root= self._insertBook(self.root, bookNum, bookName, price, num)
    
    def _insertBook(self, node, bookNum, bookName, price, num):
        if node == None:
            return Node(bookNum, bookName, price, num)
        elif bookNum < node.bookNum:
            node.left = self._insertBook(node.left, bookNum, bookName, price, num)
        elif bookNum > node.bookNum:
            node.right = self._insertBook(node.right, bookNum, bookName, price, num,)
        else: #신규 입력된 도서와 같은 "도서번호"를 가진 도서가 있는 경우 "error: 1"
            print("error: 1")
            pass
        return node
    
    #재고추가 연산
    def add(self, bookNum, num):
        return self._addBook(self.root, bookNum, num)
    
    def _addBook(self, node, bookNum, num):
        if node is None: #재고로 입력된 "도서번호"와 같은 도서번호를 가진 목록이 없는 경우 "error: 2"
            print("error: 2")
            return None
        elif bookNum == node.bookNum:
            node.num = int(node.num)
            num = int(num)
            node.num += num
            node.num = str(node.num)
            return  #return 내용물은 없애도 된다.
        elif bookNum > node.bookNum:
            return self._addBook(node.left, bookNum, num)
        else:
            return self._addBook(node.right, bookNum, num)

    #판매부수 연산
    def sale(self, bookNum, num):
        return self._saledBook(self.root, bookNum, num)
    
    def _saledBook(self, node, bookNum, num):
        if node is None: #재고로 입력된 "도서번호"와 같은 도서번호를 가진 목록이 없는 경우 "error: 2"
            print("error: 2")
            return None
        elif bookNum == node.bookNum: #판매 도서 목록 중에 동일한 key(bookNum)을 가진 목록이 있는 경우 -> 판매된 리스트를 담는 트리에 추가
            node.num = int(node.num)
            num = int(num)
            if node.num >= num: #재고수량< 판매수량인 경우: 재고수량보다 더 많은 부수를 판매할 수 없으므로
                node.num -= num
                self.rootSaled=self._insertSaledBook(node, node.bookNum, node.bookName, node.price, node.num)
            else:
                print("error: 3")
            node.num = str(node.num)
            return  #return 내용물은 없애도 된다.
        elif bookNum > node.bookNum:
            return self._saledBook(node.left, bookNum, num)
        else:
            return self._saledBook(node.right, bookNum, num)
    
    def _insertSaledBook(self, node, bookNum, bookName, price, num): #판매된 리스트를 담는 트리에 "삽입"하는 함수
        self.rootSaled = self._insertSaledBookRe(self.rootSaled, bookNum, bookName, price, num)
    
    def _insertSaledBookRe(self, node, bookNum, bookName, price, num): #판매된 리스트를 순환하며 직접 추가하는 함수
        if node == None:
            return Node(bookNum, bookName, price, num)
        elif bookNum < node.bookNum:
            node.left = self._insertBook(node.left, bookNum, bookName, price, num)
        elif bookNum > node.bookNum:
            node.right = self._insertBook(node.right, bookNum, bookName, price, num,)
        else: #신규 입력된 도서와 같은 "도서번호"를 가진 도서가 있는 경우 "판매 수량 추가"
            node.num = int(node.num)
            num = int(num)
            node.num += num #기존 node의 num(수량)에 새롭게 판매된 만큼의 num(수량) 추가
            node.num = str(node.num)
            pass
        return node
    
    #재고도서 삭제
    def delete(self, bookNum):
        self.root = self.deleteNode(self.root, bookNum)
    
    def _deleteNode(self, node, bookNum):
        if node == None:
            print("error: 2")
            return None

        if bookNum < node.bookNum:
            node.left = self._deleteNode(node.left, bookNum)
            return node

        elif bookNum > node.key:
            node.right = self._deleteNode(node.right, bookNum)
            return node
        
        else: #key(bookNum)과 동일한 도서를 찾은 경우
            if node.right == None:
                return node.left
            if node.left == None:
                return node.right
            
            rightMinNode = self._minNode(node.right)
            node.bookNum = rightMinNode.bookNum
            node.value = rightMinNode.value

            node.right = self._deleteNOde(node.right, node.bookNum)
            return node

    def _minNode(self, node): #최소키 노드를 반환하는 함수(반복)
        if node is None:
            return None
        while node.left != None:
            node = node.left
        return node

    def _minNodeRecur(self, node): #최소키 노드를 반환하는 함수(재귀)
        if node.left == None:
            return node
        else:
            return self._minNode(node.left)

    def search(self, bookNum):
        return self._searchBook(self.root, bookNum)
    
    def _searchBook(self, node, bookNum):
        if node is None: #재고로 입력된 "도서번호"와 같은 도서번호를 가진 목록이 없는 경우 "error: 2"
            print("error: 2")
            return None
        elif bookNum == node.bookNum:
            answer =[]
            answer.append(node.bookNum)
            answer.append(node.bookName)
            answer.append(node.price)
            answer.append(node.num)
            return answer 
        elif bookNum > node.bookNum:
            return self._searchBook(node.left, bookNum)
        else:
            return self._searchBook(node.right, bookNum)

    def printAll(self):
        return

    def saledInfo(self):
        return

T=BST()
while True:
    command = input().split()
    if command[0] == 'N':
        T.insert(command[1], command[2], command[3], command[4])
        # 재고에 insert: T.insert(도서번호, 도서이름, 가격, 수량)
        # 신규도서가 재고도서 목록에 있을 경우 "error: 1" 출력

    elif command[0] == 'R':
        T.add(command[1], command[2])
        # 기존에 등록된 도서의 수량이 입고: T.add(도서번호, 수량) : 덮어씌우기
        # 도서번호의 도서가 재고도서 목록에 없을 경우 "error: 2" 출력 

    elif command[0] == 'S':
        size=T.sale(command[1], command[2])
        # 판매된 도서번호와 도서 권 수 입력(Tree 내부에서 해당 key값을 찾은 뒤 업데이트 : 덮어씌우기)
        # 업데이트하면서 L을 위해 따로 리스트나 트리 생성 필요
        # 입력되는 도서번호가 재고도서 목록에 없을 경우 "error: 2" 출력
        # 판매수량이 재고수량보다 많을 경우 "error: 3" 출력

    elif command[0] == 'D':
        T.delete(command[1])
        # 재고에서 삭제: T.delete(도서번호)
        # 입력되는 도서번호가 재고도서 목록에 없을 경우 "error: 2" 출력

    elif command[0] == 'I':
        print(" ".join(T.search(command[1])))
        # 입력되는 도서번호의 재고상태(도서번호, 이름, 가격, 재고수량) 출력
        # 재고가 0일 때도 출력
        # 입력되는 도서번호가 재고도서 목록에 없을 경우 "error: 2" 출력

    elif command[0] == 'P':
        if T.printAll() == 0:
            print("Tree doesn't have any elements")
        else:
            print(" ".join(T.printAll()))
        # 재고의 원소들을 오름차순으로 출력: T.print() , "도서번호 이름 가격 재고수량" 출력 (key : 도서번호 기준 오름차순)
        # 재고가 0일 때도 출력
    
    elif command[0] == 'L':
        print(" ".join(T.SaledInfo()))
        # 판매한 모든 도서의 판매정보를 출력: T.saledInfo(), "도서번호 이름 가격 판매수량" 출력 (key : 도서번호 기준 오름차순)

    elif command[0] == 'Q':
        break
    else:
        continue