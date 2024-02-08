class Set :    # 집합 클래스
    def __init__(self) :    # 생성자
        self.items = []    # 원소를 저장하기 위한 리스트 생성

    def size(self) :    # 집합의 크기
        return len(self.items)    # len()함수 사용

    def display(self, msg) :    # 화면에 출력
        print(msg, self.items)    # 메시지 + 집합 내용 출력

    def contains(self, item) :
        return item in self.items    # item이 self.items에 있는지 검사

    def insert(self, elem) :    # 정렬된 상태를 유지하면서 elem을 삽입
        if elem in self.items : return    # 이미 있음
        for idx in range(len(self.items)) :    # loop: n번
            if elem < self.items[idx] :    # 삽입할 위치 idx를 찾음
                self.items.insert(idx, elem)    # 그 위치에 삽입
                return
        self.items.append(elem)    # 맨 뒤에 삽입

    def isEmpty(self) :    # 집합이 비어있는지 검사
        if len(self.items) == 0 : self.insert('Empty Set')    # 집합의 크기가 0이면 공집합

    def delete(self, elem) :    # 원소 제거
        if elem in self.items :    # 원소가 집합에 있으면
            self.items.remove(elem)    # 해당 원소 제거

    def __eq__(self, setB) :    # 두 집합 self, setB가 같은 집합인가?
        if self.size() != setB.size() :    # 원소의 개수가 같아야 함
            return False
        for idx in range(len(self.items)) :    # loop: n번
            if self.items[idx] != setB.items[idx] :    # 원소별로 같은지 검사
                return False
        return True

    def union(self, setB) :    # 집합 self와 집합 setB의 합집합(self U B)
        newSet = Set()    # 반환할 합집합
        a = 0    # 집합 self의 원소에 대한 인덱스
        b = 0    # 집합 setB의 원소에 대한 인덱스
        while a < len(self.items) and b < len(setB.items) :
            valueA = self.items[a]    # 집합 self의 현재 원소
            valueB = setB.items[b]    # 집합 setB의 현재 원소
            if valueA < valueB :    # self의 원소가 더 작으면
                newSet.items.append(valueA)    # 이 원소를 합집합에 추가
                a += 1    # self의 현재 원소 인덱스 증가
            elif valueA > valueB :    # setB의 원소가 더 작으면
                newSet.items.append(valueB)    # 이 원소를 합집합에 추가
                b += 1    # setB의 현재 원소 인덱스 증가
            else :    # 중복되는 원소
                newSet.items.append(valueA)    # 하나만 추가
                a += 1
                b += 1
        while a < len(self.items) :    # self에 남은 원소를 모두 추가
            newSet.items.append(self.items[a])
            a += 1
        while b < len(setB.items) :    # setB에 남은 원소를 모두 추가
            newSet.items.append(setB.items[b])
            b += 1
        return newSet    # 합집합 반환

    def intersect(self, setB) :    # 집합 self와 집합 setB의 교집합(self ^ B)
        newSet = Set()    # 반환할 교집합
        a = 0    # 집합 self의 원소에 대한 인덱스
        b = 0    # 집합 setB의 원소에 대한 인덱스
        while a < len(self.items) and b < len(setB.items) :
            valueA = self.items[a]    # 집합 self의 현재 원소
            valueB = setB.items[b]    # 집합 setB의 현재 원소
            if valueA < valueB :    # self의 원소가 더 작으면
                a += 1    # self의 현재 원소 인덱스 증가
            elif valueA > valueB :    # setB의 원소가 더 작으면
                b += 1    # setB의 현재 원소 인덱스 증가
            else :    # 중복되는 원소
                newSet.items.append(valueA)    # 하나만 추가
                a += 1
                b += 1
        newSet.isEmpty()    # 교집합이 공백인지 검사
        return newSet    # 교집합 반환

    def difference(self, setB) :    # 집합 self와 집합 setB의 차집합(self - B)
        newSet = Set()    # 반환할 차집합
        a = 0    # 집합 self의 원소에 대한 인덱스
        b = 0    # 집합 setB의 원소에 대한 인덱스
        while a < len(self.items) and b < len(setB.items) :
            valueA = self.items[a]    # 집합 self의 현재 원소
            valueB = setB.items[b]    # 집합 setB의 현재 원소
            if valueA < valueB :    # self의 원소가 더 작으면
                newSet.items.append(valueA)    # 이 원소를 합집합에 추가
                a += 1    # self의 현재 원소 인덱스 증가
            elif valueA > valueB :    # setB의 원소가 더 작으면
                b += 1    # setB의 현재 원소 인덱스 증가
            else :    # 중복되는 원소
                a += 1    # self, setB의 인덱스만 증가
                b += 1
        while a < len(self.items) :    # self에 남은 원소를 모두 추가
            newSet.items.append(self.items[a])
            a += 1
        newSet.isEmpty()    # 교집합이 공백인지 검사
        return newSet    # 차집합 반환

setA = Set()
setA.insert('휴대폰')
setA.insert('지갑')
setA.insert('손수건')
setA.display('Set A:')

setB = Set()
setB.insert('빗')
setB.insert('파이썬 자료구조')
setB.insert('야구공')
setB.insert('지갑')
setB.display('Set B:')

setB.insert('빗')
setA.delete('손수건')
setA.delete('발수건')
setA.display('Set A:')
setB.display('Set B:')

setA.union(setB).display('A U B:')
setA.intersect(setB).display('A ^ B:')
setA.difference(setB).display('A - B:')