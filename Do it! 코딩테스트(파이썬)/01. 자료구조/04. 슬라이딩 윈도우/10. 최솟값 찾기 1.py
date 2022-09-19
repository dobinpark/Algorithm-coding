from collections import deque

n, l = map(int, input().split())
my_deque = deque()
now = list(map(int, input().split()))

# 새로운 값이 들어올 때마다 정렬 대신 현재 수보다 큰 값을 덱에서 제거해 시간 복잡도를 줄임
for i in range(n):
	while my_deque and my_deque[-1][0] > now[i]:
		my_deque.pop()
	my_deque.append((now[i], i))
	if my_deque[0][1] <= i - l:  # 범위에서 벗어난 값은 덱에서 제거
		my_deque.popleft()
	print(my_deque[0][0], end=' ')
