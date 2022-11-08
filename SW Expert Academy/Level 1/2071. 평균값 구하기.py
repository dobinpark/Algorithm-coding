t = int(input())
count = 0

for i in range(1, t + 1):
	n = list(map(int, input().split()))

	for j in range(10):
		count += n[j]

	print('#' + str(i), end= ' ')
	print(round(count / 10))
	count = 0