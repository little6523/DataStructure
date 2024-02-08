def contains(bag, e) :           #bag애 항목 e가 있는지 검사하는 함수
    return e in bag              #파이썬의 in 연산자 사용
                                 
def insert(bag, e) :             #bag에 항목e를 넣는 함수
    bag.append(e)                #파이썬 리스트의 append메소드 사용
                                 
def remove(bag, e) :             #bag에서 항목 e를 삭제하는 함수
    bag.remove(e)                #파이썬 리스트의 remove메소드 사용
                                 
def count(bag) :                 #bag의 전체 항목 수를 계산하는 함수
    return len(bag)              #파이썬의 len 함수 사용

def numOf(bag, item) :
    i = 0
    n = count(bag)
    num = 0
    for i in range(n) :
        if(bag[i] == item) : num = num + 1
    return num;
                                 
myBag = []                       #Bag를 위한 빈 리스르를 만듦
                                 
insert(myBag, '휴대폰')          #Bag에 휴대폰 삽입
insert(myBag, '지갑')            #Bag에 지갑 삽입
insert(myBag, '손수건')          #Bag에 손수건 삽입
insert(myBag, '빗')              #Bag에 빗 삽입
insert(myBag, '자료구조')        #Bag에 자료구조 삽입
insert(myBag, '야구공')          #Bag에 야구공 삽입
insert(myBag, '연필')            #Bag에 연필 삽입
insert(myBag, '지우개')          #Bag에 지우개 삽입
insert(myBag, '전공책')          #Bag에 전공책 삽입
insert(myBag, '과자')            #Bag에 과자 삽입

print('가방속의 물건:', myBag)   #Bag의 내용 출력

insert(myBag, '빗')              #Bag에 빗 삽입(중복)
insert(myBag, '자료구조')        #Bag에 자료구조 삽입(중복)
remove(myBag, '손수건')          #Bag에 손수건 삭제
remove(myBag, '빗')              #Bag에 빗 삭제
print('가방속의 물건:', myBag)   #Bag의 내용 출력

print('가방속의 자료구조의 개수:', numOf(myBag, '자료구조'))
print('가방속의 빗의 개수:', numOf(myBag, '빗'))
print('가방속의 손수건의 개수:', numOf(myBag, '손수건'))