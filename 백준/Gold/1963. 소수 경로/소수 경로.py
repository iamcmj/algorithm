# 1963번 소수 경로
from collections import deque

# 자리수 이동
dx = [1, 10, 100, 1000]


def bfs(num1, num2):
    # 방문 배열 초기화
    visited = [0] * 10001
    queue = deque()
    queue.append(num1)
    res = -1

    while queue:
        x = queue.popleft()
        if x == num2:
            res = visited[x]
            break
        for i in range(4):
            # 바꿀 한 자리 선택
            curDigit = (x // dx[i]) % 10
            for j in range(0, 10):
                # 예외 처리(중요) -> 1. 첫번째 자리가 0으로 바뀔 때 2. 기존 숫자랑 같을 때
                if (i == 3 and j == 0) or (j == curDigit):
                    continue
                # 숫자 새로 조합해 확인해보기(1. 소수인지 2. 방문하지 않았는지)
                temp = x + (j - curDigit) * dx[i]
                if temp in primeNumList and not visited[temp]:
                    visited[temp] = visited[x] + 1
                    queue.append(temp)

    return res


# 소수 리스트 만들기
primeList = [True] * 10001
primeList[1] = False
primeNumList = []

for i in range(2, 101):
    if primeList[i]:
        for j in range(i * i, 10001, i):
            primeList[j] = False

for i in range(1000, 10000):
    if primeList[i]:
        primeNumList.append(i)


T = int(input())
for i in range(T):
    num1, num2 = map(int, input().split())
    res = bfs(num1, num2)
    if res == -1:
        print("Impossible")
    else:
        print(res)
