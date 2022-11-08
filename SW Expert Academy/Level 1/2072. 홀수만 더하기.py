t = int(input())
count = 0

for i in range(1, t + 1):
	n = list(map(int, input().split()))
	for j in n:
		if j % 2 != 0:
			count += j
	print('#' + str(i), count)
	count = 0
