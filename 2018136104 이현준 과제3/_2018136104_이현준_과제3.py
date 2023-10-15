class Polynomial :
    def __init__(self) :   # 생성자
        self.coef = []

    def degree(self) :   # 최고차항을 반환하는 함수
        return len(self.coef) - 1    # 최고차항은 항목수 - 1

    def ab_display(self, msg = "f(x) = ") :   # 입력 A(x), B(x) 표시 함수
        print(" ", msg, end = ' ')
        deg = self.degree()

        if self.check_zero() == 1 :   # 함수가 0인지 판단하여 0이면 0만 출력
            print("0")
        else :
            for n in range(deg, -1, -1) :
                if self.coef[n] == 0 :
                    print("             ", end = ' ')     # 계수가 0인항은 공백처리하여 자리맞춤
                elif self.coef[n] < 0 :  # 계수가 음수이면 마이너스 부호(-)를 출력하고
                    sign = "-"           # 음수인 계수를 절댓값을 취하여 양수를 만든 후 출력
                    print("%4s %.1f x^%d " %(sign, abs(self.coef[n]), n), end = ' ')
                else :                   # 계수가 양수이면 플러스 부호(+)를 출력하고
                    sign = "+"           # 계수 출력
                    print("%4s %.1f x^%d " %(sign, self.coef[n], n), end = ' ')
            print()

    def c_display(self, msg = "f(x) = ") :   # 결과 C(x) 표시 함수
        print(" ", msg, end = ' ')           # 계수가 0인 부분은 출력하지 않음
        deg = self.degree()

        if self.check_zero() == 1 :   # 함수가 0인지 판단하여 0이면 0만 출력
            print("0")
        else :
            for n in range(deg, -1, -1) :
                if self.coef[n] < 0 :     # 계수가 음수이면 마이너스 부호(-)를 출력하고
                    sign = "-"            # 음수인 계수를 절댓값을 취하여 양수를 만든 후 출력
                    print("%4s %.1f x^%d " %(sign, abs(self.coef[n]), n), end = ' ')
                elif self.coef[n] > 0 :   # 계수가 양수이면 플러스 부호(+)를 출력하고
                    sign = "+"            # 계수 출력
                    print("%4s %.1f x^%d " %(sign, self.coef[n], n), end = ' ')
            print()
             

    def deg_diff(self, b) : # 두 함수를 비교하여 최고 차항이 더 큰 함수의 최고 차항 반환
        if self.degree() > b.degree() :
           dig_diff = self.degree() - b.degree()   # 두 함수의 최고 차수의 차이를 구함

           for i in range(dig_diff) :   # 계산 시 자리를 맞추기 위해
               b.coef.append(0)         # 최고 차수가 작은 함수에 0을 추가하여
                                        # 두 함수의 최고차항을 맞춤
           return self.degree()         # 두 함수중 최고 차항이 더 큰 함수의 최고 차항 반환

        elif self.degree() < b.degree() :
            dig_diff = b.degree() - self.degree()   # 두 함수의 최고 차수의 차이를 구함

            for i in range(dig_diff) :   # 계산 시 자리를 맞추기 위해 
               self.coef.append(0)       # 최고 차수가 작은 함수에 0을 추가하여
                                         # 두 함수의 최고차항을 맞춤
            return b.degree()            # 두 함수중 최고 차항이 더 큰 함수의 최고 차항 반환

        else :
            return self.degree()         # 두 함수의 최고 차항이 같으면 그냥 반환

    def check_zero(self) :   # 함수가 0인지 검사하는 함수
        cnt = 0
        for i in range (self.degree(), -1, -1) :   # 계수가 0이 아닌 항이 나오면 검사 종료
            if self.coef[i] != 0 :
                break;
            else :                                 # 계수가 0인 항이 나올 때마다
                cnt = cnt + 1                      # 카운트를 하나씩 올림
                if cnt == self.degree() + 1 :      # '총 계산된 카운트'와 '함수의 최고차항 + 1'을 비교
                    return 1                       # 두 값이 맞으면 1 반환

    def eval(self, x) :
        sum = 0
        mul_num = 1
        for i in range(self.degree() + 1) :  # 'i'범위 설정 => 0 1 2 3 ... self.degree()
            for j in range(self.degree() - i, 0, -1) :   # 'j'범위 설정 => self.degree() ... 3 2 1 0
                mul_num = mul_num * x   # x의 제곱을 계산하여 mul_num에 입력
            sum = sum + (self.coef[self.degree() - i] * mul_num)   # x의 제곱을 계산한 후에 해당 자리의 계수를
            mul_num = 1                      # x의 제곱과 곱한 값을 sum에 더함
                                             # 그 후 mul_num을 1로 초기화 한 후 나머지 자리도 위와 똑같이 반복
        return sum
                

    def add(self, b) :   # 두 함수의 덧셈
        c = Polynomial()    # 결과를 받기 위한 c객체 생성
        c.coef = [0] * (self.deg_diff(b) + 1)   # c객체의 배열 초기화

        for i in range(self.deg_diff(b) + 1) :   # 두 함수 중 최고 차항이 더 큰 함수의 최고차항에
            c.coef[i] = self.coef[i] + b.coef[i] # +1을 한 값만큼 반복하여 두 함수를 더하여 c객체의
                                                 # 배열에 받음
        return c

    def sub(self, b) :   # 두 함수의 뺄셈
        c = Polynomial()    # 결과를 받기 위한 c객체 생성
        c.coef = [0] * (self.deg_diff(b) + 1)   # c객체의 배열 초기화

        for i in range(b.degree() + 1) :  # B(x)의 항목 개수만큼 반복하여
            c.coef[i] = b.coef[i] * (-1)  # B(x)에 -1을 곱하여 모든 항의 부호를 바꾸고 C(x)에 저장

        return self.add(c)   # A(x)와 C(x)를 더한 값을 반환

    def mul(self, b) :   # 두 함수의 곱셈
        c = Polynomial()    # 결과를 받기 위한 c객체 생성
        c.coef = [0] * (self.degree() + b.degree() + 1)   # c객체의 리스트 초기화
                                                # 이 때, 항목 수는 두 함수의 최고 차항을 더한 값에 +1을 한 값만큼 만들어야함
        for i in range(self.degree() + 1) :   # 'i'범위 설정 => 0 1 2 3 ... self.degree()     
            for j in range(b.degree() + 1) :    # 'j'범위 설정 => 0 1 2 3 ... b.degree()
                c.coef[i+j] = c.coef[i+j] + (self.coef[i] * b.coef[j])   # 두 함수의 모든 항을 곱하여 c객체 리스트에 저장

        return c


def read_poly() :   # '계산할 두 함수'를 입력받는 함수
    instr = input("최고차항부터 차수를 순서대로 입력하시오 : ")   # 함수를 입력받음
    strlist = instr.split()   # 입력 받은 함수를 공백단위로 쪼개서 strlist에 저장
    p = Polynomial()   # p 객체 생성
    for coef in strlist :   # strlist에 있는 값들을
        val = float(coef)   # float형으로 형변환 하여 val에 저장
        p.coef.insert(0, val)   # 객체 p의 리스트에 val값 저장

    return p

a = read_poly()   # A(x) 입력
b = read_poly()   # B(x) 입력
c = a.add(b)      # A(x) + B(x)를 C(x)에 저장
print("\n덧셈의 결과는 다음과 같습니다.(단, 결과 C(x)는 자리에 맞추어 표시하지 않습니다.)")
a.ab_display("A(x) = ")
b.ab_display("B(x) = ")
print("------------------------------------------------------------------------------")
c.c_display("C(x) = ")
print("  C(2) = ", c.eval(2))   # C(x)에서 x에 2를 대입한 값 출력
print("------------------------------------------------------------------------------")
print("뺄셈의 결과는 다음과 같습니다.")
c = a.sub(b)   # A(x) - B(x)를 C(x)에 저장
a.ab_display("A(x) = ")
b.ab_display("B(x) = ")
print("------------------------------------------------------------------------------")
c.c_display("C(x) = ")
print("  C(2) = ", c.eval(2))   # C(x)에서 x에 2를 대입한 값 출력
print("------------------------------------------------------------------------------")
print("곱셈의 결과는 다음과 같습니다.")
c = a.mul(b)   # A(x) * B(x)를 C(x)에 저장
a.ab_display("A(x) = ")
b.ab_display("B(x) = ")
print("------------------------------------------------------------------------------")
c.c_display("C(x) = ")
print("  C(2) = ", c.eval(2))   # C(x)에서 x에 2를 대입한 값 출력
print("------------------------------------------------------------------------------")