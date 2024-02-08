income = int(input("연봉을 입력하세요 ==> "))  #연봉(income)을 int형태로 입력받음

if income <= 1200 :                            #3~26번째 줄 : 근로소득세율 표에 따라 주어진 연봉의 세금과 세후 소득을
    tax = income * 0.06                        #조건문(if문)을 사용하여 계산
    print("전체세금 = ", tax)
    print("순수소득 = ", income - tax)

elif income <= 4600 :
    tax = 1200 * 0.06 + (income-1200) * 0.15
    print("전체세금 = ", tax)
    print("순수소득 = ", income - tax)

elif income <= 8800 :
    tax = 1200 * 0.06 + 3400 * 0.15 + (income-4600) * 0.24
    print("전체세금 = ", tax)
    print("순수소득 = ", income - tax)

elif income <= 15000 :
    tax = 1200 * 0.06 + 3400 * 0.15 + 4200 * 0.24 + (income-8800) * 0.35
    print("전체세금 = ", tax)
    print("순수소득 = ", income - tax)

else :
    tax = 1200 * 0.06 + 3400 * 0.15 + 4200 * 0.24 + 6200 * 0.35 + (income-15000) * 0.38
    print("전체세금 = ", tax)
    print("순수소득 = ", income - tax)