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

    def insert(self, key, value):
        self.root= self._insertSubtree(self.root, key, value)
    
    def _insertSubtree(self, node, key, value):
        if node == None:
            return Treenode(key, value)
        elif key < node.key:
            node.left = self._insertSubtree(node.left, key ,value) #왼쪽 자식 Node에 삽입
        elif key > node.key:
            node.right = self._insertSubtree(node.right, key, value)
        else:
            pass #pass와 continue의 차이?
        return node
        
        