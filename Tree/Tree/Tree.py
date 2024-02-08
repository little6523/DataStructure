from Queue import CircularQueue

class TNode :   # 이진트리를 위한 노드 클래스
    def __init__(self, data, left, right) :   # 생성자
        self.data = data   # 노드의 데이터
        self.left = left   # 왼쪽 자식을 위한 링크
        self.right = right   # 오른쪽 자식을 위한 링크

def preorder(n) :   # 전위 순회 함수
    if n is not None :
        print("[%c]" %(n.data), end=' ')   # 먼저 루트노드 처리(화면 출력)
        preorder(n.left)   # 왼쪽 서브트리 처리
        preorder(n.right)   # 오른쪽 서브트리 처리

def inorder(n) :   # 중위 순회 함수
    if n is not None :
        inorder(n.left)   # 왼쪽 서브트리 처리
        print("[%c]" %(n.data), end=' ')   # 루트노드 처리(화면 출력)
        inorder(n.right)   # 오른쪽 서브트리 처리

def postorder(n) :   # 후위 순회 함수
    if n is not None :
        postorder(n.left)   # 왼쪽 서브트리 처리
        postorder(n.right)   # 오른쪽 서브트리 처리
        print("[%c]" %(n.data), end=' ')   # 루트노드 처리(화면 출력)

def levelorder(root) :
    queue = CircularQueue()   # 큐 객체 초기화
    queue.enqueue(root)   # 최초에 큐에는 루트 노드만 들어있음
    while not queue.isEmpty() :   # 큐가 공백상태가 아닌 동안,
        n = queue.dequeue()   # 큐에서 맨 앞의 노드 n을 꺼냄
        if n is not None :
            print("[%c]" %(n.data), end=' ')   # 먼저 노드의 정보를 출력
            queue.enqueue(n.left)   # n의 왼쪽 자식 노드를 큐에 삽입
            queue.enqueue(n.right)   # n의 오른쪽 자식 노드를 큐에 삽입

def level(root, node) :   # 임의의 노드의 level을 구하는 함수
    if root is None :   # 해당 노드가 비어있으면
        return 0   # 0반환
    Lleft = level(root.left, node)   # 왼쪽 자식 노드 (순환 호출)
    Lright = level(root.right, node)   # 오른쪽 자식 노드 (순환 호출)
    if root is node : return 1   # 찾는 노드가 해당 노드이면 1반환
    if (Lleft > Lright) :   # 왼쪽에서 찾았으면
        return Lleft + 1   # Lleft에 1을 증가시킨 값을 반환
    elif (Lleft < Lright) :   # 오른쪽에서 찾았으면
        return Lright + 1   # Lright에 1을 증가시킨 값을 반환
    else :
        return 0   # 서로 못 찾았을 경우 0 반환

def reverse(root) :   # 이진트리를 좌우로 대칭시키는 함수
    if root is None :   # 해당 노드가 비어있으면
        return   # None 반환
    tmp = root.left   # tmp에 해당노드의 왼쪽 자식 노드 넣기
    root.left = root.right   # 왼쪽 자식 노드에 오른쪽 자식 노드 넣기
    root.right = tmp   # 오른쪽 자식노드에 tmp 넣기
    reverse(root.left)   # 왼쪽 자식 노드에 대한 순환 호출
    reverse(root.right)   # 오른쪽 자식 노드에 대한 순환 호출

def count_node(n) :   # 순환을 이용해 트리의 노드 수를 계산하는 함수
    if n is None :   # n이 None이면 공백 트리 --> 0을 반환
        return 0
    else :   # 좌우 서브트리의 노드수의 합 +1을 반환 (순환이용)
        return 1 + count_node(n.left) + count_node(n.right)

def count_leaf(n) :   # 순환을 이용해 트리의 단말 노드 수를 계산하는 함수
    if n is None :   # 공백 트리 --> 0을 반환
        return 0
    elif n.left is None and n.right is None :   # 단말노드 --> 1을 반환
        return 1
    else :   # 비단말 노드 : 좌우 서브트리의 결과 합을 반환
        return count_leaf(n.left) + count_leaf(n.right)

def calc_height(n) :   # 순환을 이용해 트리의 높이를 계산하는 함수
    if n is None :   # 공백 트리 --> 0을 반환
        return 0
    hLeft = calc_height(n.left)   # 왼쪽 트리의 높이 --> hLeft
    hRight = calc_height(n.right)   # 오른쪽 트리의 높이 --> hRight
    if (hLeft > hRight) :   # 더 높은 높이에 1을 더해 반환
        return hLeft + 1
    else :
        return hRight + 1

g1 = TNode('G', None, None)
h1 = TNode('H', None, None)
e1 = TNode('E', g1, h1)
f1 = TNode('F', None, None)
d1 = TNode('D', None, None)
b1 = TNode('B', d1, None)
c1 = TNode('C', e1, f1)
root1 = TNode('A', b1, c1)

print('\n    In-Order : ', end='')
inorder(root1)
print('\n   Pre-Order : ', end='')
preorder(root1)
print('\n  Post-Order : ', end='')
postorder(root1)
print('\n Level-Order : ', end='')
levelorder(root1)
print()
print(" 노드의 개수 = %d개" % count_node(root1))
print(" 단말의 개수 = %d개" % count_leaf(root1))
print(" 트리의 높이 = %d" % calc_height(root1))
print("----------------------------------------------------------------------")

a2 = TNode('A', None, None)
b2 = TNode('B', None, None)
div2 = TNode('/', a2, b2)
c2 = TNode('C', None, None)
mul2_1 = TNode('*', div2, c2)
d2 = TNode('D', None, None)
mul2 = TNode('*', mul2_1, d2)
e2 = TNode('E', None, None)
root2 = TNode('+', mul2, e2)

print('\n    In-Order : ', end='')
inorder(root2)
print('\n   Pre-Order : ', end='')
preorder(root2)
print('\n  Post-Order : ', end='')
postorder(root2)
print('\n Level-Order : ', end='')
levelorder(root2)
print()
print(" 노드의 개수 = %d개" % count_node(root2))
print(" 단말의 개수 = %d개" % count_leaf(root2))
print(" 트리의 높이 = %d" % calc_height(root2))
print("----------------------------------------------------------------------")

c3 = TNode('C', None, None)
d3 = TNode('D', None, None)
b3 = TNode('B', c3, d3)
f3 = TNode('F', None, None)
e3 = TNode('E', None, f3)
root3 = TNode('A', b3, e3)

print('Level-Order : ', end='')
levelorder(root3)
reverse(root3)
print()
print("노드의 레벨은 %d 입니다." % level(root3, root3))
print("노드의 레벨은 %d 입니다." % level(root3, b3))
print("노드의 레벨은 %d 입니다." % level(root3, c3))
print("노드의 레벨은 %d 입니다." % level(root3, d3))
print("노드의 레벨은 %d 입니다." % level(root3, e3))
print("노드의 레벨은 %d 입니다." % level(root3, f3))
print(" 트리의 좌우를 교환 합니다.")
print('Level-Order : ', end='')
levelorder(root3)
print()