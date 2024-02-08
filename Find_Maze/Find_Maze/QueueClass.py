MAX_QSIZE = 10
class CircularQueue :
    def __init__(self) : 
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE

    def isEmpty(self) : return self.front == self.rear
    def isFull(self) : return self.front == (self.rear + 1) % MAX_QSIZE
    def clear(self) : self.front = self.rear

    def enqueue(self, item) :
        if not self.isFull() :
            self.rear = (self.rear + 1) % MAX_QSIZE
            self.items[self.rear] = item

    def dequeue(self) :
        if not self.isEmpty() :
            self.front = (self.front + 1) % MAX_QSIZE
            return self.items[self.front]

    def peek(self) :
        if not self.isEmpty() :
            return self.items[(self.front + 1) % MAX_QSIZE]

    def size(self) :
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE

    def display(self) :
        out = []
        if self.front < self.rear :
            out = self.items[self.front + 1 : self.rear + 1]
        else :
            out = self.items[self.front + 1 : MAX_QSIZE] + self.items[0:self.rear + 1]
        print("[f=%s,r=%d] ==> "%(self.front, self.rear), out)

class PriorityQueue :
    def __init__(self) :     # 생성자 : 객체를 생성하면서 items리스트 생성
        self.items = []

    def isEmpty(self) :      # 리스트가 공백인지 검사하는 함수
        return len(self.items) == 0

    def size(self) : return len(self.items)     # 리스트의 크기를 반환하는 함수
    
    def clear(self) : self.items = []     # 리스트를 공백상태로 만드는 함수

    def sort_list(self) :     # 리스트의 항목을 우선순위순으로 정렬해주는 함수(버블정렬)
         if self.isEmpty() : return None
         else :
             size = self.size()
             for i in range(0, self.size()) :
                 for j in range(0, size - 1) :
                     if self.items[j][2] < self.items[j+1][2] :     # j+1번째 항목이 j번째보다 크면
                         tmp = self.items[j]                        # j번째 항목을 tmp에 넣고
                         self.items[j] = self.items[j+1]            # j+1번째 항목을 j번째에 넣고
                         self.items[j+1] = tmp                      # tmp를 j+1번째 항목에 넣음
                 size = size - 1

    def enqueue(self, item) :       # 리스트에 항목을 넣는 함수
        self.items.append(item)
        self.sort_list()

    def dequeue(self) :      # 리스트에서 우선순위가 가장 높은 항목 꺼내고 반환하는 함수
        return self.items.pop(0)

    def peek(self) :      # 리스트에서 우선순위가 가장 높은 항목을 반환하는 함수
        return self.items[0][2]