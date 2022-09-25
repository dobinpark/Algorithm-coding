import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[] for i in range(n + 1)]
visited = [False] * (n + 1)


def dfs(v):
	visited[v] = True
	for i in a[v]:
		if not visited[i]:
			dfs(i)


for _ in range(m):
	s, e = map(int, input().split())
	a[s].append(e)
	a[e].append(s)

count = 0

for i in range(1, n + 1):
	if not visited[i]:
		count += 1
		dfs(i)

print(count)
