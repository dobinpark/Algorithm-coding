t = int(input())

for i in range(1, t + 1):
	a, b = map(int, input().split())
	c = a + b
	print("Case #{0}: {1}".format(i, c))
