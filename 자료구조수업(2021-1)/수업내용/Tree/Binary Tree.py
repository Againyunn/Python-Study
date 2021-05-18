class TNode:
    def __init__(self): #값을 입력 받지 않은 경우 None으로 초기값 자동 설정
        self.data=data
        self.left=left
        self.right=right

class BinaryTree:
    def __init__(self):
        self.root = None

    def binarySearch(self, a, key): #반복문 활용 이진탐색
        left =0
        right = len(a)-1

        while left <= right:
            mid = (left + right) //2

            if key == a[mid]:
                return True
            elif key < a[mid]:
                right = mid -1
            else:
                left = mid + 1
            return False

    def binarySearchRecur(self, a, key, left, right): #재귀 활용 이진탐색
        if left > right:
            return False
        else:
            mid = (left + right)//2

            if key == a[mid]:
                return True
            elif key < a[mid]:
                return binarySearchRecur(a, key, left, mid -1 )
            else:
                return binarySearchRecur(a, key, mid +1, right )

    def height(self):
        return self._subtreeHeight(self.root)

    def _subtreeHeight(self, p):
        if p is None:
            return 0
        else:
            hleft=self._subtreeHeight(p.left)
            hright=self._subtreeHeight(p.right)
            return max(hleft, hright) +1 #recursion에 따라 각 높이를 추가 하기 위한 작업(각각의 subtree 내의 root 높이 중첩 연산)

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

    def preorder(self):
        self._subtreePreorder(self.root)
    
    def _subtreePreorder(self, p):
        if p is not None:
            print(p.data)
            self._subtreePreorder(self.left)
            self._subtreePreorder(self.right)

    def inorder(self):
        self._subtreeInorder(self.root)

    def _subtreeInorder(self,p):
        if p is not None:
            self._subtreeInorder(self.left)
            print(p.data)
            self._subtreeInorder(self.right)

    def postorder(self):
        self._subtreePostorder(self.root)

    def _subtreePostorder(self, p):
        if p is not None:
            self._subtreePostorder(self.left)
            self._subtreePostorder(self.right)
            print(p.data)

