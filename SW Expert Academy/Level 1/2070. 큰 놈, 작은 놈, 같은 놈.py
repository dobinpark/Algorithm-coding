t = int(input())

for i in range(1, t + 1):
	n, m = map(int, input().split())

	if n > m:
		print('#' + str(i), '>')
	elif n < m:
		print('#' + str(i), '<')
	elif n == m:
		print('#' + str(i), '=')
		