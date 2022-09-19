from collections import deque

n = int(input())
my_queue = deque()

for i in range(1, n + 1):
	my_queue.append(i)

while len(my_queue) > 1:                 # 카드가 1장 남을 때까지
	my_queue.popleft()                   # 맨 위의 카드를 버림
	my_queue.append(my_queue.popleft())  # 맨 위의 카드를 가장 아래 카드 밑으로 이동

print(my_queue[0])                       # 마지막으로 남은 카드 출력
