t = int(input())

for i in range(1, t + 1):
	n = input()
	if n == n[::-1]:
		print('#%d' %i, 1)
	else:
		print('#%d' %i, 0)
