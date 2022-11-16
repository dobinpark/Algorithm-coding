t = int(input())

for i in range(1, t + 1):
	n = list(map(int, input().split()))
	max_num = n[0]
	min_num = n[0]

	for j in range(len(n)):
		if max_num <= n[j]:
			max_num = n[j]
		if min_num >= n[j]:
			min_num = n[j]
	n.remove(max_num)
	n.remove(min_num)

	print('#' + str(i), round(sum(n) / len(n)))
