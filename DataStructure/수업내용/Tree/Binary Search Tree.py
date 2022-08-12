class Treenode:
    def __init__ (self, key, value, left = None, right = None):
        self.key = key #노드의 크기(index Number)
        self.value = value #노드에 담을 데이터
        self.left = left #왼쪽 주소
        self.right = right #오른쪽 주소
    
class BST:
    def __init__ (self):
        self.root = None
    def saerch1(self, key): #반복문 활용 탐색
        node = self.root
        while node is not None: #leaf node 이후에 None 값을 갖는 node가 아닐 경우 반복 순환(if문들에 의해 대상이 되는 node가 바뀜)
            if key == node.key:
                return node.value
            elif key < node.key:
                return node.left
            else:
                return node.right
    
    def search2(self, key): #재귀 활용 탐색(main)
        return self._searchBst(self.root, key)
    
    def _searchBst(self, node, key): #재귀 활용 탐색(recursion)
        if node is None:
            return None
        elif key == node.key:
            return node.value
        elif key < node.key:
            return _searchBst(node.left, key)
        else:
            return _searchBst(node.right, key)

    def maximum(self): #반복 활용 최대값 찾기
        node=self.root
        if node is None:
            return None
        while node.right != None:
            node = node.right
        return node.key

    def minimum(self): #반복 활용 최소값 찾기
        node=self.root
        if node is None:
            return None
        while node.left != None:
            node = node.left
        return node.key

    def maximumRecursion(self): #재귀 활용 최대값 찾기
        return self._maximumRe(self.root)

    def _maximumRe(self,node):
        if (node.right and node.left) == None:
            return node.key
        else:
            return self._maximumRe(node.right)

    def insert(self, key, value): #재귀 활용 삽입 기능 구현
        self.root= self._insertSubtree(self.root, key, value) #왜 root 값으로 재귀 함수를 넣는 지 원리 이해 필요.
    
    def _insertSubtree(self, node, key, value):
        if node == None:
            return Treenode(key, value)
        elif key < node.key:
            node.left = self._insertSubtree(node.left, key ,value) #왼쪽 자식 Node에 삽입
        elif key > node.key:
            node.right = self._insertSubtree(node.right, key, value)
        else:
            pass #pass와 continue의 차이? 
        #pass 는 실행할 코드가 없다는 의미(정말 코드를 넘긴다는 의미)
        #continue 는 다음 loop를 실행한다는 의미(다음 순환 코드로 넘어간다.)
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
            return self._minNodeRecur(node.left)
        
    def delete(self, key):
        self.root = self.deleteNode(self.root, key)
    
    def _deleteNode(self, node, key):
        if node == None:
            return None

        if key < node.key:
            node.left = self._deleteNode(node.left, key)
            return node

        elif key > node.key:
            node.right = self._deleteNode(node.right, key)
            return node
        
        else:
            if node.right == None:
                return node.left
            if node.left == None:
                return node.right
            
            rightMinNode = self._minNode(node.right)
            node.key = rightMinNode.key
            node.value = rightMinNode.value

            node.right = self._deleteNode(node.right, node.key)
            return node

            
'''
Tree=BST()
Tree.insert(10,'-1')
Tree.insert(9,'-1')
#Tree.insert(11,'-1')
Tree.insert(8,'-1')
Tree.insert(13,'0')
Tree.insert(12,'0')
a1=Tree.maximum()
a2=Tree.maximumRecursion()
print(a1)
print(a2)
'''

