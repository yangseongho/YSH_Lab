
# 코드 8.1: 이진트리를 위한 노드 클래스
class TNode:
    def __init__ (self, elem, left, right):
        self.data = elem
        self.left = left
        self.right = right

    def isLeaf(self):
        return self.left is None and self.right is None

# 코드 8.2: 이진트리의 전위순회
def preorder(n) :
    if n is not None :
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)

# 코드 8.3: 이진트리의 중위순회
def inorder(n) :
    if n is not None :
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)

# 코드 8.4: 이진트리의 후위순회
def postorder(n) :
    if n is not None :
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')

# 코드 8.5: 이진트리의 레벨순회
from CircularQueue import CircularQueue

def levelorder(root) :
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None :
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

# 코드 8.6: 이진트리의 노드 수 계산
def count_node(n) :
    if n is None :
        return 0
    else :
        return 1 + count_node(n.left) + count_node(n.right)

# 코드 8.7: 이진트리의 단말노드 수 계산
def count_leaf(n) :
    if n is None : return 0
    elif n.isLeaf() : return 1
    else : return count_leaf(n.left) + count_leaf(n.right)


# 코드 8.8: 이진트리의 트리의 높이 계산
def calc_height(n) :
    if n is None : return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight) : return hLeft + 1
    else: return hRight + 1

# 기타 연산들
def evaluate(n) :
    if n is None :
       return 0
    elif n.left is None and n.right is None :
       return n.data
    else :
        op1 = evaluate(n.left)
        op2 = evaluate(n.right)
        if n.data == '+' : return op1 + op2
        elif n.data == '-' : return op1 - op2
        elif n.data == '*' : return op1 * op2
        elif n.data == '/' : return op1 / op2

def calc_size(n) :
    if n is None :
        return 0
    else :
        return n.data + calc_size(n.left) + calc_size(n.right)


def delete_node(root, key):
    if root is None:
        return None  # 트리가 비어있을 경우

    # 삭제할 키가 현재 노드와 일치하는 경우
    if root.data == key:
        # 리프 노드인 경우 (자식이 없는 노드)
        if root.left is None and root.right is None:
            return None
        # 한쪽 자식만 있는 경우
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            # 두 자식이 모두 있는 경우
            # 오른쪽 서브트리에서 최소값을 찾음
            min_larger_node = find_min(root.right)
            root.data = min_larger_node.data  # 최소값으로 현재 노드 대체
            # 최소값 노드를 삭제
            root.right = delete_node(root.right, min_larger_node.data)

    elif key < root.data:
        root.left = delete_node(root.left, key)
    else:
        root.right = delete_node(root.right, key)

    return root


# 오른쪽 서브트리에서 최소값 노드를 찾는 함수
def find_min(node):
    while node.left is not None:
        node = node.left
    return node



#=========================================================
#   - 이 파일이 직접 실행될 때에는 다음 문장들을 실행함.
#   - 다른 파일에서 모듈로 불려지는 경우는 실행되지 않음.
#=========================================================
# 테스트 프로그램
if __name__ == "__main__":
    print("\n======= 이진트리 테스트 ===================================")
    d = TNode('D', None, None)
    e = TNode('E', None, None)
    b = TNode('B', d, e)
    f = TNode('F', None, None)
    c = TNode('C', f, None)
    root = TNode('A', b, c)

    print('\n   In-Order : ', end='')
    inorder(root)
    print('\n  Pre-Order : ', end='')
    preorder(root)
    print('\n Post-Order : ', end='')
    postorder(root)
    print('\nLevel-Order : ', end='')
    levelorder(root)
    print()

    print(" 노드의 개수 = %d개" % count_node(root))
    print(" 단말의 개수 = %d개" % count_leaf(root))
    print(" 트리의 높이 = %d" % calc_height(root))
    print("\n======= 노드 삭제 테스트 ==================================")
    keys_to_delete = ['C', 'A', 'B']  # 삭제할 키 목록
    for key in keys_to_delete:
        print(f"\n노드 '{key}' 삭제 후:")
        root = delete_node(root, key)
        print("   In-Order : ", end='')
        inorder(root)
        print("\n  Pre-Order : ", end='')
        preorder(root)
        print("\n Post-Order : ", end='')
        postorder(root)
        print("\nLevel-Order : ", end='')
        levelorder(root)
        print()

        print(" 노드의 개수 = %d개" % count_node(root))
        print(" 단말의 개수 = %d개" % count_leaf(root))
        print(" 트리의 높이 = %d" % calc_height(root))


