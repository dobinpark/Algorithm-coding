n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
	if x > a[i]:
		print(a[i], end=' ')
