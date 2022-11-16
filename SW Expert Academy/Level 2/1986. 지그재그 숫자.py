t = int(input())

for i in range(1, t + 1):
	n = int(input())
	m = 0
	for j in range(1, n + 1):
		if j % 2 == 0:
			m -= j
		else:
			m += j

	print('#' + str(i), m)
