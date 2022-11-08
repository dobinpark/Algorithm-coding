t = int(input())
count = 0

for i in range(t):
	if t <= 0:
		break
	j = t % 10
	t = int(t / 10)
	count += j

print(count)

# 또는 print( sum([int(x) for x in input()]))
# 한 줄로 끝남.
