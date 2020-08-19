# N개 입력받기
n = int(input())
array = [0]*1000000

# 가게에 있는 전체 부품번호를 입력받아 기록
for i in input().split():
    array[int(i)] = 1

# M개 입력받기
m = int(input())
want = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in want:
    # 해당 부품이 존재한다면
    if array[i] == 1:
        print('yes', end=' ')
    # 해당 부품이 존재하지 않다면
    else:
        print('no', end=' ')