# 18352번 특정 거리의 도시 찾기
from collections import deque
import sys

input = sys.stdin.readline


def bfs(graph, queue, dist):
    while queue:
        num = queue.popleft()
        for neighbor in graph[num]:
            if dist[neighbor] == -1:
                queue.append(neighbor)
                dist[neighbor] = dist[num] + 1


N, M, K, X = map(int, input().split())
graph = [[] for i in range(N + 1)]
dist = [-1] * (N + 1)
dist[X] = 0

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

queue = deque([X])
bfs(graph, queue, dist)

res = []
for i in range(1, N + 1):
    if dist[i] == K:
        res.append(i)

if len(res) == 0:
    print(-1)
else:
    print(*res, sep="\n")
