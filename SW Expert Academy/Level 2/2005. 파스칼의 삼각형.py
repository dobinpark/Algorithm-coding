t = int(input())

for tc in range(1, t + 1):
	n = int(input())
	num = []
	for i in range(1, n + 1):
		num.append([1] * i) # 처음에 1로 다 채워주기

	for i in range(0, n):
		if i >= 2: # 행이 i 인덱스 2이상일 때만 들어감
			for j in range(1, len(num[i]) - 1): # 맨 처음이랑 맨 마지막 범위를 제외하고
				num[i][j] = num[i - 1][j] + num[i -1][j - 1] # 자기 자신보다 위에 인덱스 값  +왼위 인덱스 값

	print('#' + str(tc))

	for i in range(n):
		print(*num[i])
