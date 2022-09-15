x = int(input())
n = int(input())
total = 0

for i in range(n):
	a, b = map(int, input().split())
	c = a * b
	# 합계를 중첩
	total += c

if total == x:
	print("Yes")
elif total != x:
	print("No")
