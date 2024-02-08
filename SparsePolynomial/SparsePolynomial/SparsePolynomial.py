from LinkedList import LinkedList

class Term :    # 다항식의 항을 나타내는 클래스
    def __init__(self, expo, coef) :
        self.expo = expo    # 항의 차수
        self.coef = coef    # 항의 계수

class SparsePoly(LinkedList) :    # 희소 다항식 클래스
    def __init__(self) :     # LinkedList의 생성자를를 상속받는 생성자
        super().__init__()

    def degree(self) :    # 최고 차항을 반환 하는 함수
        if self.head is None : return False
        else : return self.head.data.expo

    def large_degree(self, polyB) :    # A와 B 둘 중에서 더 높은 차수를 가진 객체의 차수 반환
        if self.head.data.expo >= polyB.head.data.expo :
            return self.head.data.expo
        else :
            return polyB.head.data.expo

    def zero_check(self) :    # 항이 전부 0인지 검사하는 함수
        node = self.head
        while node is not None :
            if node.data.coef != 0 : return False
            node = node.link
        return True

    def read(self) :    # 사용자 입력 함수
        self.clear()
        while True :
            token = input("계수 차수 입력(종료-1): ").split(" ")
            if token[0] == '-1' :
                self.display("입력 다항식:")
                return
            self.insert(self.size(), Term(int(token[1]), float(token[0])))

    def display(self, msg="") :    # 화면 출력 함수
        print("\t", msg, end = '')

        node = self.head
        if self.zero_check() == True : print(" 0")    # 먼저 모든 항이 0인 검사
        else :
            while node is not None :    # 계수 앞에 양수면 +, 음수면 -를 붙임
                if node.data.coef > 0 :
                    sign = '+'
                elif node.data.coef < 0 :
                    sign = '-'
                print("%4s %.1f x^%d" %(sign, abs(node.data.coef), node.data.expo), end = '')
                node = node.link
            print()

    def add(self, polyB) :    # 두 함수 A, B를 더하는 함수
        node_A = self.head     # node_A는 A의 head를 가리킴
        node_B = polyB.head    # node_B는 B의 head를 가리킴
        comp_degree = A.large_degree(B)    # A와 B 둘 중 차수가 더 높은 함수의 차수를 받음
        C = SparsePoly()    # 결과 값을 받을 C를 만듦

        while comp_degree >= 0 :    # comp_degree가 0이 될 때까지
            search_A = 0    # 함수 A에서 차수가 comp_degree인 항을 찾으면 1이됨
            search_B = 0    # 함수 B에서 차수가 comp_degree인 항을 찾으면 1이됨
            for i in range(self.size(), 0, -1) :    # A에서 차수가 comp_degree인 항을 탐색
                if node_A.data.expo == comp_degree :
                    Aexpo = node_A.data.expo
                    Acoef = node_A.data.coef
                    search_A = 1    # 찾으면 search_A = 1
                    break
                node_A = node_A.link
                if node_A is None :    # 못찾으면 node_A가 다시 A의 head를 가리킴
                    node_A = self.head
                    break

            for j in range(polyB.size(), 0, -1) :    # B에서 차수가 comp_degree인 항을 탐색
                if node_B.data.expo == comp_degree :
                    Bexpo = node_B.data.expo
                    Bcoef = node_B.data.coef
                    search_B = 1    # 찾으면 search_B = 1
                    break
                node_B = node_B.link
                if node_B is None :    # 못찾으면 node_B가 다시 B의 head를 가리킴
                    node_B = polyB.head
                    break

            if search_A == 1 and search_B == 1 :    # A, B둘다 찾았을 경우
                C.insert(C.size(), Term(Aexpo, (Acoef + Bcoef)))

            elif search_A == 1 and search_B == 0 :    # A만 찾았을 경우
                C.insert(C.size(), Term(Aexpo, Acoef))

            elif search_A == 0 and search_B == 1 :    # B만 찾았을 경우
                C.insert(C.size(), Term(Bexpo, Bcoef))

            comp_degree = comp_degree - 1    # 반복문이 돌아갈 때 마다 comp_degree가 1씩 감소

        return C

    def sub(self, polyB) :    # 두 함수 A, B를 더하는 함수
        import copy    # deecopy를 사용하기 위함
        node_B = polyB.head    # node_B는 B의 head를 가리킴
        C = copy.deepcopy(B)    # B를 C에 복사함
        node_C = C.head    # node_B는 B의 head를 가리킴
        for i in range (C.size(), 0, -1) :    # B의 모든 항의 부호를 바꾸어서 C에 저장
            node_C.data.coef = node_C.data.coef * (-1)
            node_C = node_C.link
            if node_C is None : break

        return self.add(C)    # A와 C를 더한 값을 반환

    def mul(self, polyB) :    # 두 함수 A, B를 곱하는 함수
        C = SparsePoly()
        node_A = self.head    # node_A는 A의 head를 가리킴
        node_B = polyB.head    # node_B는 B의 head를 가리킴

        while node_B is not None :    # A의 첫 항과 B의 모든 항을 곱한 값을 C에 삽입 -> C를 초기화 시킴
            C.insert(C.size(), Term((node_A.data.expo + node_B.data.expo), (node_A.data.coef * node_B.data.coef)))
            node_B = node_B.link

        node_A = node_A.link    # node_A는 다음 노드를 가리킴
        node_B = polyB.head    # node_B는 다시 B의 head를 가리킴
        node_C = C.head    # node_C는 C의 head를 가리킴
        pos_C = 0    # node_C 의 처음 위치 = 0

        while node_A != None :    # node_A가 None이 되기 전까지 반복
            if node_B == None :    # node_B가 None이면
                node_B = polyB.head    # node_B는 다시 B의 head를 가리킴
                node_A = node_A.link    # node_A는 다음 노드를 가리킴
                if node_A == None :    # node_A가 None이면 계산이 끝남
                    break
            if node_A.data.expo + node_B.data.expo > node_C.data.expo :    
                # A의 항의 차수와 B의 항의 차수를 더한 값이 C의 항보다 크면
                C.insert(pos_C, Term((node_A.data.expo + node_B.data.expo), (node_A.data.coef * node_B.data.coef)))
                # 해당 항의 이전 노드에 삽입
                node_B = node_B.link    # node_B는 다음 노드를 가리킴
                node_C = C.head    # node_C는 C의 head를 가리킴
                pos_C = 0    # node_C 의 위치 초기화
            elif node_A.data.expo + node_B.data.expo == node_C.data.expo :
                # A의 항의 차수와 B의 항의 차수를 더한 값이 C의 항과 같으면
                node_C.data.coef += (node_A.data.coef * node_B.data.coef)
                # A의 항의 계수와 B의 항의 계수를 곱한 값을 C의 계수에 더함
                node_B = node_B.link    # node_B는 다음 노드를 가리킴
                node_C = C.head    # node_C는 C의 head를 가리킴
                pos_C = 0    # node_C 의 위치 초기화
            else :    # A의 항의 차수와 B의 항의 차수를 더한 값이 C의 항보다 작으면
                node_C = node_C.link    # node_C는 다음 노드를 가리킴
                pos_C += 1    # node_C 의 위치 +1 
                if node_C == None :    # node_C가 None이면
                    C.insert(pos_C, Term((node_A.data.expo + node_B.data.expo), (node_A.data.coef * node_B.data.coef)))
                    # C의 맨 뒤 노드(None)에 삽입
                    node_B = node_B = node_B.link    # node_B는 다음 노드를 가리킴
                    node_C = C.head    # node_C는 C의 head를 가리킴
                    pos_C = 0    # node_C 의 위치 초기화

        return C

A = SparsePoly()
B = SparsePoly()
A.read()
B.read()
C = A.add(B)
A.display("  A =")
B.display("  B =")
C.display("A+B =")
C = A.sub(B)
C.display("A-B =")
C = A.mul(B)
C.display("A*B =")