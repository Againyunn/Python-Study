stockBook =[] #재고를 저장할 전역변수 stockBook로 임의의 빈 리스트 선언
saledBook =[] #판매이력을 저장할 전역변수 stockBook로 임의의 빈 리스트 선언

class Node: #재고 도서의 데이터를 담아두는 트리
    def __init__ (self, bookNum, bookName = None, price = None, num = None, left = None, right = None):
        self.bookNum = bookNum #key 값
        self.bookName = bookName
        self.price = price
        self.num = num
        self.left = left
        self.right = right

class saledNode: #판매된 도서 데이터를 담아두는 트리
    def __init__ (self, bookNum, bookName = None, price = None, num = None):
        self.bookNum = bookNum #key 값
        self.bookName = bookName
        self.price = price
        self.num = num

class BST: #이진탐색트리
    def __init__ (self):
        self.root = None #재고도서의 root
        self.rootSaled = None #판매도서의 root
    
    #신규등록 연산
    def insert(self, bookNum, bookName, price, num): 
        self.root= self._insertBook(self.root, bookNum, bookName, price, num)
    
    def _insertBook(self, node, bookNum, bookName, price, num): #재귀연산을 통해 수강자의 학번이 추가될 노드의 위치를 찾고 삽입하는 함수
        if node == None: #재고도서 Node 생성
            return Node(bookNum, bookName, price, num)
        elif bookNum < node.bookNum:
            node.left = self._insertBook(node.left, bookNum, bookName, price, num)#왼쪽 자식 Node 탐색
        elif bookNum > node.bookNum:
            node.right = self._insertBook(node.right, bookNum, bookName, price, num,)#오른쪽 자식 Node 탐색
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
            return 
        elif bookNum == node.bookNum:
            node.num = int(node.num)
            num = int(num)
            node.num += num
            node.num = str(node.num)
            return  
        elif bookNum < node.bookNum: #왼쪽 자식 Node 탐색
            return self._addBook(node.left, bookNum, num)
        else: #오른쪽 자식 Node 탐색
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
            if node.num >= num: #재고수량> 판매수량인 경우:
                node.num -= num #판매 부수만큼 Node의 num 줄이기
                num = str(num)
                self.rootSaled = self._insertSaledBook(node, node.bookNum, node.bookName, node.price, num)#판매된 부수 Saledbook트리 추가 num : 판매된 도서 부수
            else: #재고수량< 판매수량인 경우: 재고수량보다 더 많은 부수를 판매할 수 없으므로 "error: 3"
                print("error: 3")
            node.num = str(node.num)
            return  
        elif bookNum < node.bookNum: #왼쪽 자식 Node 탐색
            return self._saledBook(node.left, bookNum, num)
        else: #오른쪽 자식 Node 탐색
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
        self.root = self._deleteNode(self.root, bookNum)
    
    def _deleteNode(self, node, bookNum): #재귀연산을 통해 각 노드의 "키"(bookNum) 비교를 통하여 삭제 명령을 받은 수강자 Node를 찾고 삭제하는 함수
        if node == None: #bookNum과 일치하는 Node가 없는 경우
            print("error: 2")
            return 

        if bookNum < node.bookNum:
            node.left = self._deleteNode(node.left, bookNum) #왼쪽 자식 Node 탐색
            return node

        elif bookNum > node.bookNum:
            node.right = self._deleteNode(node.right, bookNum) #오른쪽 자식 Node 탐색
            return node
        
        else: #key(bookNum)과 동일한 도서를 찾은 경우
            if node.right == None: #경우1: 오른쪽 자식 Node가 없는 경우
                return node.left
            if node.left == None: #경우2: 왼쪽 자식 Node가 없는 경우
                return node.right

            #경우3: 해당 노드가 Subtree의 root Node인 경우
            rightMinNode = self._minNode(node.right) #현재 Node의 right subtree의 최소 값(rightMinNode) 재귀이용
            node.bookNum = rightMinNode.bookNum #삭제할 대상 Node의 "키"(bookNum)를 rightMinNode의 bookNum으로 변경
            node.bookName = rightMinNode.bookName
            node.price = rightMinNode.price
            node.num = rightMinNode.num

            node.right = self._deleteNode(node.right, node.bookNum)  #삭제한 노드의 right subtree의 root 노드를 지정(재귀)
            return node

    def _minNode(self, node): #최소키 노드를 반환하는 함수(반복)
        if node is None:
            return None
        while node.left != None:
            node = node.left
        return node

    #재고검색 연산
    def search(self, bookNum): #사용자로부터 검색할 bookNum을 입력받을 함수
        return self._searchBook(self.root, bookNum)
    
    def _searchBook(self, node, bookNum): #재귀검색을 통해 bookNum에 일치하는 값을 반환할 함수
        if node is None: #재고로 입력된 "도서번호"와 같은 도서번호를 가진 목록이 없는 경우 "error: 2"
            print("error: 2")
            return 
        elif bookNum == node.bookNum: #재고로 입력된 bookNum과 동일한 도서번호를 가진 노드를 찾은 경우
            answer =[] #노드의 데이터들을 저장할 임의의 빈 리스트
            answer.append(node.bookNum)
            answer.append(node.bookName)
            answer.append(node.price)
            answer.append(node.num)
            return answer
        elif bookNum < node.bookNum:  #왼쪽 자식 Node 탐색
            return self._searchBook(node.left, bookNum)
        else: #오른쪽 자식 Node 탐색
            return self._searchBook(node.right, bookNum)

    def printAll(self): #재고도서 출력함수
        global stockBook #재고목록의 책을 담을 임시 전역변수 stockBook

        self._stockBookPreorder(self.root) #전위순회로 모든 노드의 값을 불러오기
        if stockBook!=[]: # stockBook에 노드가 저장된 경우
            list(set([tuple(set(i))for i in stockBook])) #2차원 리스트의 중복 제거
            stockBook.sort() #오름차순 정렬
            answer = stockBook
            stockBook = [] #stockBook리스트 초기화(다음 printAll 호출 대비)
        else: #stockBook에 노드가 없는 경우
            answer= 0
        return answer

    def _stockBookPreorder(self, node):#재고도서 전위순회
        global stockBook #재고목록의 책을 담을 임시 전역변수 stockB ook

        if node is not None: #빈노드가 아니라면 전위순회
            temp = [] #임시 리스트(2차원 배열로 만들기 위해 각 Node의 데이터를 1차원 리스트로 저장)
            temp.append(node.bookNum)
            temp.append(node.bookName)
            temp.append(node.price)
            temp.append(node.num)
            stockBook.append(temp) #stcokBook에 temp(현재 Node의 데이터) 추가
            self._stockBookPreorder(node.left)
            self._stockBookPreorder(node.right)

    def saledInfo(self): #판매도서 출력함수
        global saledBook #판매목록의 책을 담을 임시 전역변수 saledBook

        self._saledBookPreorder(self.rootSaled) #전위순회로 모든 노드의 값 불러오기
        if saledBook!=[]:#saledBook에 판매된 도서 원소들이 추가된 경우
            list(set([tuple(set(i))for i in saledBook])) #2차원 리스트의 중복제거
            saledBook.sort() #오름차순 정렬
            answer = saledBook
            saledBook = [] #saledBook리스트 초기화(다음 saledInfo 호출 대비)
        else: #stockBook에 노드가 없는 경우
            answer= 0
        return answer

    def _saledBookPreorder(self, node):#판매도서 전위순회
        global saledBook #판매목록의 책을 담을 임시 전역변수 saledBook

        if node is not None: #빈노드가 아니라면 전위순회
            temp = [] #임시 리스트(2차원 배열로 만들기 위해 각 Node의 데이터를 1차원 리스트로 저장)
            temp.append(node.bookNum)
            temp.append(node.bookName)
            temp.append(node.price)
            temp.append(node.num)
            saledBook.append(temp) #saledkBook에 temp(현재 Node의 데이터) 추가
            self._saledBookPreorder(node.left)
            self._saledBookPreorder(node.right)

T=BST()
while True:
    command = input().split()
    if command[0] == 'N': #완
        T.insert(command[1], command[2], command[3], command[4])
        # 재고에 insert: T.insert(도서번호, 도서이름, 가격, 수량)
        # 신규도서가 재고도서 목록에 있을 경우 "error: 1" 출력

    elif command[0] == 'R': #완
        T.add(command[1], command[2])
        # 기존에 등록된 도서의 수량이 입고: T.add(도서번호, 수량) : 덮어씌우기
        # 도서번호의 도서가 재고도서 목록에 없을 경우 "error: 2" 출력 

    elif command[0] == 'S': #50% 완 -> saledNode로 입력이 되는 지만 확인되면 완료
        size=T.sale(command[1], command[2])
        # 판매된 도서번호와 도서 권 수 입력(Tree 내부에서 해당 key값을 찾은 뒤 업데이트 : 덮어씌우기)
        # 업데이트하면서 L을 위해 따로 리스트나 트리 생성 필요
        # 입력되는 도서번호가 재고도서 목록에 없을 경우 "error: 2" 출력
        # 판매수량이 재고수량보다 많을 경우 "error: 3" 출력

    elif command[0] == 'D': #완
        T.delete(command[1])
        # 재고에서 삭제: T.delete(도서번호)
        # 입력되는 도서번호가 재고도서 목록에 없을 경우 "error: 2" 출력

    elif command[0] == 'I': #완
        try:
            print(" ".join(T.search(command[1])))
        except TypeError:
            pass
        # 입력되는 도서번호의 재고상태(도서번호, 이름, 가격, 재고수량) 출력
        # 재고가 0일 때도 출력
        # 입력되는 도서번호가 재고도서 목록에 없을 경우 "error: 2" 출력

    elif command[0] == 'P': #완
        if T.printAll() == 0:
            pass
        else:
            result = T.printAll()
            for i in result:
                print(" ".join(i))
        # 재고의 원소들을 오름차순으로 출력: T.print() , "도서번호 이름 가격 재고수량" 출력 (key : 도서번호 기준 오름차순)
        # 재고가 0일 때도 출력
    
    elif command[0] == 'L': 
        if T.saledInfo() == 0:
            pass
        else:
            result = T.saledInfo()
            for i in result:
                print(" ".join(i))
        #print(" ".join(T.saledInfo()))
        # 판매한 모든 도서의 판매정보를 출력: T.saledInfo(), "도서번호 이름 가격 판매수량" 출력 (key : 도서번호 기준 오름차순)

    elif command[0] == 'Q': 
        break
        #프로그램 종료
    else:
        continue