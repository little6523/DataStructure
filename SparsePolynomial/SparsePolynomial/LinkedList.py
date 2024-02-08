class Node :
    def __init__ (self, elem, next=None) :
        self.data = elem
        self.link = next

class LinkedList :    # 연결된 리스트 클래스
    def __init__(self) :
        self.head = None

    def isEmpty(self) : return self.head == None    # 공백상태 검사
    def clear(self) : self.head = None    # 리스트 초기화
    def size(self) :    # 리스트의 항목의 수 반환
        node = self.head
        count = 0
        while not node == None :
            node = node.link
            count += 1
        return count

    def display(self, msg = 'LinkedList : ') :    # 내용 출력
        print(msg, end = '')
        node = self.head
        while not node == None :
            print(node.data, end = '')
            node = node.link
        print()

    def getNode(self, pos) :    # pos번째 노드 반환
        if pos < 0 : return None
        node = self.head    # node는 head부터 시작
        while pos > 0 and node != None :    # pos번 반복
            node = node.link    # node를 다음 노드로 이동
            pos -= 1    # 남은 반복 횟수 줄임
        return node    # 최종 노드 반환

    def getEntry(self, pos) :    # pos번째 노드의 데이터 반환
        node = self.getNode(pos)    # pos번째 노드
        if node == None : return None    # 찾는 노드가 없는 경우
        else : return node.data    # 그 노드의 데이터 필드 반환

    def replace(self, pos, elem) :    # pos번째 노드의 데이터를 변경
        node = self.getNode(pos)    # pos번째 노드를 찾아
        if node != None : node.data = elem    # 데이터 필드에 elem 복사

    def find(self, data) :    # 데이터로 data를 갖는 노드 반환
        node = self.head
        while node is not None :    # 모든 노드에서 찾음
            if node.data == data : return node    # 찾아지면 바로 반환
            node = node.link
        return node    # 찾아지지 않으면 None 반환

    def insert(self, pos, elem) :    # 노드 삽입
        before = self.getNode(pos-1)    # before 노드를 찾음
        if before == None :    # 맨 앞에 삽입하는 경우
            self.head = Node(elem, self.head)    # 맨 앞에 삽입함
        else :    # 중간에 앞에 삽입하는 경우
            node = Node(elem, before.link)    # 노드 생성 + Step1
            before.link = node    # Step2

    def delete(self, pos) :    # 노드 삭제
        before = self.getNode(pos-1)    # before 노드를 찾음
        if before == None :    # 시작노드를 삭제
            if self.head is not None :    # 공백이 아니면
                self.head = self.head.link    # head를 다음으로 이동
        elif before.link != None :    # 중간에 있는 노드 삭제
            before.link = before.link.link    # Step1
            