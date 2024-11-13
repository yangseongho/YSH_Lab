from BinaryTree import *
from BinSrchTree import *

def calc_height(n) :
    if n is None : return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight) : return hLeft + 1
    else: return hRight + 1

# 코드 9.13: 노드의 균형인수 계산 함수
def calc_height_diff(n) :
    if n==None :
       return 0
    return calc_height(n.left) - calc_height(n.right)

# 코드 9.14: AVL 트리의 LL회전     
def rotateLL(A) :
	B = A.left
	A.left = B.right
	B.right = A
	return B

# 코드 9.15: AVL 트리의 RR회전     
def rotateRR(A) :
	B = A.right
	A.right = B.left
	B.left = A
	return B

# 코드 9.16: AVL 트리의 RL회전
def rotateRL(A) :
	B = A.right
	A.right = rotateLL(B)
	return rotateRR(A)

# 코드 9.17: AVL 트리의 LR회전
def rotateLR(A) :
	B = A.left
	A.left = rotateRR(B)
	return rotateLL(A)

# 코드 9.18: AVL 트리의 재균형 함수
def reBalance (parent) :
	hDiff = calc_height_diff(parent)

	if hDiff > 1 :
		if calc_height_diff( parent.left ) > 0 :
			parent = rotateLL( parent )
		else :
			parent = rotateLR( parent )
	elif hDiff < -1 :
		if calc_height_diff( parent.right ) < 0 :
			parent = rotateRR( parent )
		else :
			parent = rotateRL( parent )
	return parent

# 코드 9.19: AVL 트리의 삽입 연산
def insert_avl(parent, node) :
    if node.key < parent.key :
        if parent.left != None :
            parent.left = insert_avl(parent.left, node)
        else :
            parent.left = node
        return reBalance(parent)

    elif node.key > parent.key :
        if parent.right != None :
            parent.right = insert_avl(parent.right, node)
        else :
            parent.right = node
        return reBalance(parent);
    else :
        print("중복된 키 에러")


# AVL 트리에서의 삭제 연산
def delete_avl(root, key):
    if root is None:
        return root

    # 1. 삭제할 노드를 찾기
    if key < root.key:
        root.left = delete_avl(root.left, key)
    elif key > root.key:
        root.right = delete_avl(root.right, key)
    else:  # key == root.key (삭제할 노드를 찾았음)
        # 2. 자식이 없는 경우 (단말 노드)
        if root.left is None and root.right is None:
            root = None
        # 3. 자식이 하나인 경우
        elif root.left is None:
            root = root.right
        elif root.right is None:
            root = root.left
        # 4. 자식이 둘인 경우
        else:
            min_node = find_min(root.right)
            root.key = min_node.key
            root.right = delete_avl(root.right, min_node.key)

    # 5. 트리가 균형을 유지하도록 재균형
    if root is None:
        return root

    # 트리의 균형이 맞지 않으면 회전하여 균형을 맞춘다.
    return reBalance(root)

# 최소값 노드 찾기 (삭제 후 후계자 찾을 때 사용)
def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

from CircularQueue import CircularQueue

def levelorder(root) :
    queue = CircularQueue(100)
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None :
            print(n.key, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)



# 코드 9.20: AVL 트리 테스트 프로그램 (삭제 연산 포함)
if __name__ == "__main__":
    node = [7, 8, 9, 2, 1, 5, 3, 6, 4]
    root = None
    for i in node:
        n = BSTNode(i)
        if root is None:
            root = n
        else:
            root = insert_avl(root, n)
        print("AVL(%d): " % i, end='')
        levelorder(root)
        print()

    print("삭제 연산을 테스트합니다.")
    # 예시: 키 3을 삭제
    root = delete_avl(root, 3)
    print("키 3을 삭제한 후: ", end='')
    levelorder(root)
    print()

    # 또 다른 삭제 테스트: 키 8 삭제
    root = delete_avl(root, 8)
    print("키 8을 삭제한 후: ", end='')
    levelorder(root)
    print()

    # 삭제 후 트리의 상태 출력
    print(" 노드의 개수 =", count_node(root))
    print(" 단말의 개수 =", count_leaf(root))
    print(" 트리의 높이 =", calc_height(root))


