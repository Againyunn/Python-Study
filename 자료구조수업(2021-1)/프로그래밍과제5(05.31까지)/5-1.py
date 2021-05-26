BinarySearchTree =[] #출력할 Node를 임시로 담아둘 임의의 전역변수 BinarySearchTree에 빈 리스트 선언

class Node:
    def __init__ (self,st_id, left = None, right = None):
        self.st_id = st_id #수강자의 학번(key값)
        self.left = left #왼쪽 자식 노드의 주소
        self.right = right #오른쪽 자식 노드의 주소
    
class BST:
    
    def __init__ (self):
        self.root = None #초기값 

    def insert(self, st_id): #사용자로부터 수강자 학번을 입력 받는 함수
        self.root = self._insertSub(self.root, st_id)
    
    def _insertSub(self, node, st_id): #재귀연산을 통해 수강자의 학번이 추가될 노드의 위치를 찾고 삽입하는 함수
        if node == None:
            return Node(st_id) #수강자 학번 Node 생성
        elif st_id < node.st_id: 
            node.left = self._insertSub(node.left, st_id) #왼쪽 자식 Node 탐색
        elif st_id > node.st_id:
            node.right = self._insertSub(node.right, st_id) #오른쪽 자식 Node 탐색
        else:
            pass 
        return node

    def delete(self, st_id): #사용자로부터 수강신청 취소할 수강자 학번을 입력 받는 함수
        self.root = self._deleteNode(self.root, st_id)
    
    def _deleteNode(self, node, st_id): #재귀연산을 통해 각 노드의 "키"(st_id) 비교를 통하여 삭제 명령을 받은 수강자 Node를 찾고 삭제하는 함수
        if node == None: #st_id와 일치하는 Node가 없는 경우
            return None

        if st_id < node.st_id: 
            node.left = self._deleteNode(node.left, st_id) #왼쪽 자식 Node 탐색
            return node

        elif st_id > node.st_id:
            node.right = self._deleteNode(node.right, st_id) #오른쪽 자식 Node 탐색
            return node
        
        else: #st_id와 동일한 "키"값을 갖는 Node를 찾은 경우
            if node.right == None: #경우1: 오른쪽 자식 Node가 없는 경우
                return node.left
            if node.left == None: #경우2: 왼쪽 자식 Node가 없는 경우
                return node.right
            
            #경우3: 해당 노드가 Subtree의 root Node인 경우
            rightMinNode = self._minNode(node.right) #현재 Node의 right subtree의 최소 값(rightMinNode) 재귀이용
            node.st_id = rightMinNode.st_id #삭제할 대상 Node의 "키"(st_id)를 rightMinNode의 st_id로 변경

            node.right = self._deleteNode(node.right, node.st_id) #삭제한 노드의 right subtree의 root 노드를 지정(재귀)
            return node
    
    def _minNode(self, node): #최소키 노드를 반환하는 함수(재귀)
        if node.left == None:
            return node
        else:
            return self._minNode(node.left)
    
    def size(self): #사용자가 수강신청한 수강자의 "수"를 구하는 함수(재귀)
        return self._subtreeSize(self.root)

    def _subtreeSize(self, p): #Node의 수를 재귀 반복하며 구하는 함수
        if p is None: #basecase
            return 0
        else:
            return 1 + self._subtreeSize(p.left) + self._subtreeSize(p.right)

    def printAll(self): #수강신청한 수강자의 정보(st_id)를 반환
        global BinarySearchTree #전역 변수 BinarySearchTree 사용 선언

        self._subtreePreorder(self.root) #전위순회(재귀)
        if BinarySearchTree!=[]: #BinarySearchTree에 원소가 있는 경우
            temp = set(BinarySearchTree) #set으로 변환하여 중복원소 제거
            BinarySearchTree = list(temp) #list 형태로 데이터형 변환
            BinarySearchTree.sort() #오름차순 정렬
            answer = BinarySearchTree
            BinarySearchTree = []
        else:
            answer= 0 #BinarySearchTree에 원소가 없는 경우(Node가 없는 경우)
        return answer

    def _subtreePreorder(self, node): #전위순회하며 각 Node의 st_id를 반환
        global BinarySearchTree#전역 변수 BinarySearchTree 사용 선언

        if node is not None:
            BinarySearchTree.append(node.st_id) #BinarySearchTree에 각 Node의 st_id를 추가
            self._subtreePreorder(node.left)
            self._subtreePreorder(node.right)

T=BST() #BST클래스의 인스턴스 T 선언

#수강신청 프로그램(while 무한 루프)
while True:
    command = input().split()
    # st_id(즉, command[1])를 수강자리스트에 insert: T.insert(command[1])
    if command[0] == 'N':
        T.insert(command[1])
    
    # st_id(즉, command[1])를 수강자리스트에서 삭제: T.delete(command[1])
    elif command[0] == 'C':
        T.delete(command[1])
    
     # 수강자리스트의 원소 수를 출력: T.size() 출력
    elif command[0] == 'S':
        size=T.size()
        print(size)

    # 수강자리스트의 원소들을 오름차순으로 출력: T.print()
    elif command[0] == 'P':
        if T.printAll() == 0:
            pass
        else:
            print(" ".join(T.printAll()))
    
    #프로그램 종료
    elif command[0] == 'Q':
        break

    else:
        continue