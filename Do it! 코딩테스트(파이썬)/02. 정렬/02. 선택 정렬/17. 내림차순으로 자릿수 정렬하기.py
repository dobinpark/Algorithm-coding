import sys

print = sys.stdout.write
a = list(input())

for i in range(len(a)):
	max = i
	for j in range(i + 1, len(a)):
		if a[j] > a[max]:
			max = j

	if a[i] < a[max]:
		temp = a[i]
		a[i] = a[max]
		a[max] = temp

for i in range(len(a)):
	print(a[i])
