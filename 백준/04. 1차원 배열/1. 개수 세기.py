n = int(input())
m = list(map(int, input().split()))
v = int(input())
count = 0

for i in range(n):
	if m[i] == v:
		count += 1

print(count)