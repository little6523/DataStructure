import random        # random 함수를 사용하기 위함

answer = random.randint(0, 99)  # 0부터 99까지의 정수 중 무작위의 한 정수를 정함

min = 0        # min, max, cnt : 최솟값과 최댓값, 시도 횟수 초기화
max = 99
cnt = 1

for i in range(10) :     # 반복문(for문)과 조건문(if문)을 이용하여 예측한 숫자와 정답을 비교
    print("숫자를 입력하세요(범위:%d~%d) : " %(min, max), end="")
    guess = int(input())
    if answer == guess :
        print(" 정답입니다. %d번 만에 맞추셨습니다." %(cnt))
        break
    elif answer > guess :
        print("아닙니다. 더 큰 숫자입니다!")
        min = guess
    elif answer < guess :
        print("아닙니다. 더 작은 숫자입니다!")
        max = guess
    cnt = cnt + 1

print(" 게임이 끝났습니다. 정답은 %d 입니다." %(answer))    # 게임 종료 문구 출력