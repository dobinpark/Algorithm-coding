n = int(input())
ans = [0] * n
a = list(map(int, input().split()))
my_stack = []

for i in range(n):
	# 스택이 비어 있지 않고 현재 수열이 스택 top 인덱스가 가리키는 수열보다 클 경우
	while my_stack and a[my_stack[-1]] < a[i]:
		ans[my_stack.pop()] = a[i]  # 정답 리스트에 오큰수를 현재 수열로 저장하기
	my_stack.append(i)

while my_stack:  # 반복문을 다 돌고 나왔는데 스택이 비어 있지 않다면 비울 때까지
	ans[my_stack.pop()] = -1

result = ""

for i in range(n):
	result += str(ans[i]) + " "

print(result)
