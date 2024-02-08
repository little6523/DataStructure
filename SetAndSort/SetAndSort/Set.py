class Set :
    def __init__(self) :
        self.items = []

    def size(self) :
        return len(self.items)

    def display(self, msg) :
        print(msg, self.items)

    def contains(self, item) :
        return item in self.items

    def insert(self, elem) :
        if elem in self.items : return
        for idx in range(len(self.items)) :
            if elem < self.items[idx] :
                self.items.insert(idx, elem)
                return
        self.items.append(elem)

    def __eq__(self, setB) :
        if self.size() != setB.size() :
            return False
        for idx in range(len(self.items)) :
            if self.items[idx] != setB.items[idx] :
                return False
        return True

    def delete(self, elem) :
        if elem in self.items :
            self.items.remove(elem)

    def union(self, setB) :    # 집합 self와 집합 selfB의 합집합(self U B)
        newSet = Set()
        a = 0
        b = 0
        while a < len(self.items) and b < len(setB.items) :
            valueA = self.items[a]
            valueB = setB.items[b]
            if valueA < valueB :
                newSet.items.append(valueA)
                a += 1
            elif valueA > valueB :
                newSet.items.append(valueB)
                b += 1
            else :
                newSet.items.append(valueA)
                a += 1
                b += 1
        while a < len(self.items) :
            newSet.itmes.append(self.items[a])
            a += 1
        while b < len(setB.items) :
            newSet.items.append(setB.items[b])
            b += 1
        return newSet

    def intersect(self, setB) :    # 집합 self와 집합 selfB의 교집합(self ^ B)
        newSet = Set()
        newSet.items.append(self.items)
        newSet.items.append(setB.items)
        newSet.delete(self.union(setB))
        return newSet

    def difference(self, setB) :
        setC = Set()
        for elem in self.items :
            if elem not in setB.items :
                setC.items.append(elem)
        return setC

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
