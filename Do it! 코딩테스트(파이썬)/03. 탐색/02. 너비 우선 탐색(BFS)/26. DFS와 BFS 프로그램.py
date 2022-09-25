from collections import deque

n, m, start = map(int ,input().split())
a = [[] for _ in range(n + 1)]

for _ in range(m):
	s, e = map(int, input().split())
	a[s].append(e)  # 양방향 에지이므로 양쪽에 에지를 더하기
	a[e].append(s)


# 번호가 작은 노드부터 방문하기 위해 정렬하기
for i in range(n + 1):
	a[i].sort()


def dfs(v):
	print(v, end=' ')
	visited[v] = True
	for i in a[v]:
		if not visited[i]:
			dfs(i)


visited = [False] * (n + 1)
dfs(start)


def bfs(v):
	queue = deque()
	queue.append(v)
	visited[v] = True
	while queue:
		now_Node = queue.popleft()
		print(now_Node, end=' ')
		for i in a[now_Node]:
			if not visited[i]:
				visited[i] = True
				queue.append(i)


print()
visited = [False] * (n + 1)  # 리스트 초기화
bfs(start)
