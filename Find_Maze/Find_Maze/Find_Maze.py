maze = [ ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['e', '0', '0', '0', '1', '0', '1', '0', '0', '1'],
        ['1', '0', '1', '0', '1', '0', '1', '1', '0', '1'],
        ['1', '0', '1', '0', '1', '0', '0', '0', '0', '1'],
        ['1', '0', '1', '0', '1', '0', '1', '0', '1', '1'],
        ['1', '0', '1', '0', '0', '0', '1', '0', '1', '1'],
        ['1', '0', '1', '0', '1', '0', '1', '0', '1', '1'],
        ['1', '0', '1', '0', '1', '0', '1', '0', '0', 'x'],
        ['1', '0', '1', '0', '1', '0', '1', '1', '1', '1'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'] ]    # 10x10크기의 미로
MAZE_SIZE = 10    # 미로의 크기는 10

def isValidPos(x, y) :    # 미로 밖을 벗어나지 못하게 하는 함수
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE :    # 미로 밖을 벗어나게 되면 False반환
        return False
    else :
        return map[y][x] == '0' or map[y][x] == 'x'    # 미로에서 이동할 수 있는 칸이 있으면 True반환
##########################################################################
from StackClass import Stack

def DFS() :    # 깊이우선탐색 함수
    stack = Stack()     # 사용할 스택 객체를 준비
    stack.push( (0,1) )     # 시작위치 삽입. (0,1)은 튜플
    print('DFS: ')

    while not stack.isEmpty() :    # 공백이 아닐 동안
        here = stack.pop()         # 항목을 꺼냄(pop)
        print(here, end = '->')
        x, y = here              # 스택에 저장된 튜플은 (x, y) 순서임
        if (map[y][x] == 'x') : return True     # 출구이면 탐색 성공. True 반환

        else : 
            map[y][x] = '.'     # 현재위치를 지나왔다고 '.' 표시
            if isValidPos(x, y - 1) : stack.push((x, y - 1)) # 상
            if isValidPos(x, y + 1) : stack.push((x, y + 1)) # 하
            if isValidPos(x - 1, y) : stack.push((x - 1, y)) # 좌
            if isValidPos(x + 1, y) : stack.push((x + 1, y)) # 우
    return False     # 탐색 실패. False 반환

import copy
map = copy.deepcopy(maze)    # 미로의 변경을 방지하기 위해 미로의 복사본 사용
result = DFS()
if result :
   print(' --> 미로탐색 성공')
   print()
else :
   print(' --> 미로탐색 실패')
   print()
#################################################################################
from QueueClass import CircularQueue

def BFS() :     # 넓이우선탐색 함수
    que = CircularQueue()     # 사용할 원형큐 객체를 준비
    que.enqueue( (0,1) )      # 시작위치 삽입. (0,1)은 튜플
    print('BFS: ')

    while not que.isEmpty() :     # 공백이 아닐 동안
        here = que.dequeue()      # 항목을 꺼냄(dequeue)
        print(here, end='->')
        (x, y) = here             # 원형큐에 저장된 튜플은 (x, y) 순서임
        if(map[y][x] == 'x') : return True     # 출구이면 탐색 성공. True 반환

        else :
            map[y][x] = '.'      # 현재위치를 지나왔다고 '.' 표시
            if isValidPos(x, y - 1) : que.enqueue((x, y - 1)) # 상
            if isValidPos(x, y + 1) : que.enqueue((x, y + 1)) # 하
            if isValidPos(x - 1, y) : que.enqueue((x - 1, y)) # 좌
            if isValidPos(x + 1, y) : que.enqueue((x + 1, y)) # 우
    return False

map = copy.deepcopy(maze)    # 미로의 변경을 방지하기 위해 미로의 복사본 사용
result = BFS()
if result :
   print(' --> 미로탐색 성공')
   print()
else : 
    print(' --> 미로탐색 실패')
    print()
###############################################################################
from QueueClass import PriorityQueue

import math
(ox,oy) = (9, 7)     # 출구좌표=> ox = 9, oy = 7
def dist(x, y) :
    (dx, dy) = (ox-x, ox-y)    # 출구좌표에서 현좌표값을 뺀 값 => dx = ox-x, dy = oy-y
    return math.sqrt(dx*dx + dy*dy)    # x좌표값과 y좌표값을 제곱하여 더한 후 루트를 취하여 거리계산

def MySmartSearch() :
    q = PriorityQueue()    # 사용할 우선순위큐 객체를 준비
    q.enqueue((0,1,-dist(0,1)))      # 시작위치 삽입. ( 0, 1, 거리(-dist(0,1)) )은 튜플
    print('MySmartSearch: ')

    while not q.isEmpty() :
        here = q.dequeue()      # 항목을 꺼냄(dequeue)
        print(here[0:2], end='->')
        x,y,_ = here             # 우선순위큐에 저장된 튜플은 ( 0, 1, 거리(-dist(0,1)) ) 순서임
        if(map[y][x] == 'x') : return True     # 출구이면 탐색 성공. True 반환
        else :
            map[y][x] = '.'      # 현재위치를 지나왔다고 '.' 표시
            if isValidPos(x, y - 1) : q.enqueue((x, y - 1, -dist(x, y - 1))) # 상
            if isValidPos(x, y + 1) : q.enqueue((x, y + 1, -dist(x, y + 1))) # 하
            if isValidPos(x - 1, y) : q.enqueue((x - 1, y, -dist(x - 1, y))) # 좌
            if isValidPos(x + 1, y) : q.enqueue((x + 1, y, -dist(x + 1, y))) # 우
    return False

map = copy.deepcopy(maze)    # 미로의 변경을 방지하기 위해 미로의 복사본 사용
result = MySmartSearch()
if result :
   print(' --> 미로탐색 성공')
   print()
else :
   print(' --> 미로탐색 실패')
   print()