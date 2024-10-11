# 2583번 영역 구하기
from collections import deque


def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    # 처음 방문 -> count 1로
    graph[b][a] = 1
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 이웃한 곳이 0이면 방문했다는 의미로 1로
            if 0 <= nx < N and 0 <= ny < M and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                queue.append((nx, ny))
                count += 1
    return count


M, N, K = map(int, input().split())
# 직사각형 기준 그래프
graph = [[0] * N for _ in range(M)]
# x, y축 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 2차원 배열 x, y축 주의
for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    # 영역 채우기
    for j in range(y1, y2):
        for k in range(x1, x2):
            graph[j][k] = 1

count = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            count.append(bfs(graph, j, i))

count.sort()
print(len(count))
print(*count)
