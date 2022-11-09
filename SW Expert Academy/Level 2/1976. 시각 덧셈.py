t = int(input())

for i in range(1, t + 1):
	n = list(map(int, input().split()))

	h = n[0] + n[2]
	m = n[1] + n[3]

	if m > 59:
		h = h + 1
		m = m - 60

	if h > 12:
		h = h - 12

	print('#' + str(i), h, m)
