t = int(input())

for i in range(1, t + 1):
	n = int(input())
	m = list(map(int, input().split()))

	max_value = m[-1]
	count = 0

	for j in range(n - 2, -1, -1):
		if m[j] >= max_value:
			max_value = m[j]
		else:
			count += max_value - m[j]

	print('#' + str(i), count)
