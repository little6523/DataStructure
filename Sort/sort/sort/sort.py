def printStep(arr, val) :   # 중간 과정 출력용 함수
    print(" Step %2d =" % val, end='')
    print(arr)

def bubble_sort(A) :   # 버블 정렬
    n = len(A)
    for i in range(n-1, 0, -1) :   # 외부 루프 : n-1, n-2, ... 2, 1
        bChanged = False
        for j in range(i) :   # 내부 루프 : 0, 1, ... I-1
            if (A[j]>A[j+1]) :   # 순서가 맞지 않으면
                A[j], A[j+1] = A[j+1], A[j]   # 교환!
                bChanged = True   # 교환이 발생했음

        if not bChanged: break   # 교환이 없으면 종료
        printStep(A, n - i)   # 중간 과정 출력용 문장 

def ascending_check(A) :   # 오름차순 검사 함수
    n = len(A)   # 배열 A의 크기를 n에 저장
    bChanged = False   # 배열에서는 처음 아무것도 안바뀜
    for i in range(n-1, 0, -1) :   # 외부 루프 : n-1, n-2, ... 2, 1
        for j in range(i) :   # 내부 루프 : 0, 1, ... I-1
            if (A[j]>A[j+1]) :   # 순서가 맞지 않으면
                bChanged = True   # 교환이 발생했음

    if bChanged: return False   # 교환이 있으면 False 반환
    else : return True   # 교환이 없으면 True 반환

def print_sort_check(a) :   # 오름차순 검사 결과 출력 함수
    if ascending_check(a) : print("오름차순으로 정렬되어 있습니다.")
    else : print("오름차순으로 정렬되어 있지 않습니다.")

a = [9, 2, 7, 4, 5, 6, 3, 8, 1]

print_sort_check(a)
bubble_sort(a)
print_sort_check(a)