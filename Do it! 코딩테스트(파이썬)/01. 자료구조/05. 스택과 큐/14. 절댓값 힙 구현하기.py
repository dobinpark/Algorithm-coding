from queue import PriorityQueue
import sys

print = sys.stdin.write
input = sys.stdin.readline
n = int(input())
my_queue = PriorityQueue()

for i in range(n):
	request = int(input())
	if request == 0:
		if my_queue.empty():
			print('0\n')
		else:
			temp = my_queue.get()
			print(str((temp[1])) + '\n')
	else:
		# 절댓값을 기준으로 정렬하고, 같으면 음수 우선 정렬하도록 구성
		my_queue.put((abs(request), request))
