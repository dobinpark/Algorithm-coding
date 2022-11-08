t = int(input())

for i in range(1, t + 1):
	n = map(int, input().split())
	print('#' + str(i), max(n))
