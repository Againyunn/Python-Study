BinarySearchTree =[]

class Node:
    def __init__ (self,st_id, left = None, right = None):
        self.st_id = st_id
        self.left = left
        self.right = right
    
class BST:
    #global BinarySearchTree
    
    def __init__ (self):
        self.root = None

    def insert(self, st_id):
        self.root = self._insertSub(self.root, st_id)
    
    def _insertSub(self, node, st_id):
        if node == None:
            return Node(st_id)
        elif st_id < node.st_id:
            node.left = self._insertSub(node.left, st_id) #왼쪽 자식 Node에 삽입
        elif st_id > node.st_id:
            node.right = self._insertSub(node.right, st_id)
        else:
            pass #pass와 continue의 차이? 
        #pass 는 실행할 코드가 없다는 의미(정말 코드를 넘긴다는 의미)
        #continue 는 다음 loop를 실행한다는 의미(다음 순환 코드로 넘어간다.)
        return node

    def delete(self, st_id):
        self.root = self._deleteNode(self.root, st_id)
    
    def _deleteNode(self, node, st_id):
        if node == None:
            return None

        if st_id < node.st_id:
            node.left = self._deleteNode(node.left, st_id)
            return node

        elif st_id > node.st_id:
            node.right = self._deleteNode(node.right, st_id)
            return node
        
        else:
            if node.right == None:
                return node.left
            if node.left == None:
                return node.right
            
            rightMinNode = self._minNode(node.right)
            node.st_id = rightMinNode.st_id

            node.right = self._deleteNode(node.right, node.st_id)
            return node
    
    def _minNode(self, node): #최소키 노드를 반환하는 함수(재귀)
        if node.left == None:
            return node
        else:
            return self._minNode(node.left)
    
    def size(self):
        return self._subtreeSize(self.root)

    def _subtreeSize(self, p):
        if p is None:
            return 0
        else:
            return 1 + self._subtreeSize(p.left) + self._subtreeSize(p.right)
    
    def _subtreeCountLeaf(self, p):
        if p is None:
            return 0
        elif p.left is None and p.right is None: #leaf 노드 인 경우
            return 1
        else:
            return self._subtreeCountLeaf(p.left) + self._subtreeCountLeaf(p.right)

    def printAll(self):
        global BinarySearchTree

        self._subtreePreorder(self.root)
        if BinarySearchTree!=[]:
            temp = set(BinarySearchTree)
            BinarySearchTree = list(temp)
            BinarySearchTree.sort()
            answer = BinarySearchTree
            BinarySearchTree = []
        else:
            answer= 0
        return answer

    def _subtreePreorder(self, node):
        global BinarySearchTree

        if node is not None:
            BinarySearchTree.append(node.st_id)
            self._subtreePreorder(node.left)
            self._subtreePreorder(node.right)

T=BST()
while True:
    command = input().split()
    if command[0] == 'N':
        T.insert(command[1])
       # st_id(즉, command[1])를 수강자리스트에 insert: T.insert(command[1]) 
    elif command[0] == 'C':
        T.delete(command[1])
       # st_id(즉, command[1])를 수강자리스트에서 삭제: T.delete(command[1])
    elif command[0] == 'S':
        size=T.size()
        print(size)
       # 수강자리스트의 원소 수를 출력: T.size() 출력
    elif command[0] == 'P':
        if T.printAll() == 0:
            pass#print(0)
        else:
            print(" ".join(T.printAll()))
       # 수강자리스트의 원소들을 오름차순으로 출력: T.print()
    elif command[0] == 'Q':
        break
    else:
        continue