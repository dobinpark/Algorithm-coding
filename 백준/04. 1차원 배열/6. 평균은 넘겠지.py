b = []

for k in range(int(input())):
	a = list(map(int, input().split()))
	avg = sum(a[1:]) / (len(a) - 1)
	cut = 0
	percent = 0

	for i in range(1, len(a)):
		if a[i] > avg:
			cut += 1

	percent = cut / a[0] * 100
	b.append(percent)

for i in b:
	# %를 문자로 나타내기 위해서는 앞에 %를 하나 더 붙여야함
	print('%.3f%%' % i)
