n = int(input())
a = list(map(int, input().split()))
s = [0] * n

for i in range(1, n):
	insert_point = i
	insert_value = a[i]
	for j in range(i - 1, -1, -1):
		if a[j] < a[i]:
			insert_point = j + 1
			break
		if j == 0:
			insert_point = 0
	for j in range(i, insert_point, -1):
		a[j] = a[j - 1]
	a[insert_point] = insert_value

s[0] = a[0]

for i in range(1, n):
	s[i] = s[i - 1] + a[i]

sum = 0

for i in range(0, n):  # 합 배열 총합 구하기
	sum += s[i]

print(sum)