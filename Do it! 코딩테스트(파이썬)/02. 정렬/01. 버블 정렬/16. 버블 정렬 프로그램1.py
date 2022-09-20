import sys

input = sys.stdin.readline

n = int(input())
a = []

for i in range(n):
	a.append((int(input()), i))

max = 0
sorted_a = sorted(a)

for i in range(n):
	if max < sorted_a[i][1] - i:
		 max = sorted_a[i][1] - 1

print(max + 1)
