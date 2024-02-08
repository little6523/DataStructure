class Bag :      # Bag클래스 선언
    def __init__(self) :   # Bag의 생성자
        self.bag = []      # Bag의 생성자를 호출하면서 하나의 배열 생성

    def insert(self, e) :  # Bag클래스 내의 배열에 e항목 추가
        self.bag.append(e)
                                 
    def remove(self, e) :  # Bag클래스 내의 배열에 e항목 제거
        self.bag.remove(e)

myBag = Bag()     # Bag클래스 호출
myBag.insert('휴대폰')     # myBag에 휴대폰, 지갑, 손수건 등 물건 추가
myBag.insert('지갑')
myBag.insert('손수건')
myBag.insert('빗')
myBag.insert('자료구조')
myBag.insert('야구공')
print('내 가방속의 물건:', myBag.bag)   # myBag의 물건들 출력

myBag.insert('빗')       # myBag에 빗 추가
myBag.remove('손수건')   # myBag에 손수건 제거
print('내 가방속의 물건:', myBag.bag)   # myBag의 물건들 출력