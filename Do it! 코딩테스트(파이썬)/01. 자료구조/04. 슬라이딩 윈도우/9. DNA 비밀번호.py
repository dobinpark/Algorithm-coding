check_list = [0] * 4
my_list = [0] * 4
check_secret = 0

# 함수 정의
def my_add(c):  # 새로 들어온 문자를 처리하는 함수

	global check_list, my_list, check_secret

	if c == 'A':
		my_list[0] += 1
		if my_list[0] == check_list[0]:
			check_secret += 1

	elif c == 'C':
		my_list[1] += 1
		if my_list[1] == check_list[1]:
			check_secret += 1

	elif c == 'G':
		my_list[2] += 1
		if my_list[2] == check_list[2]:
			check_secret += 1

	elif c == 'T':
		my_list[3] += 1
		if my_list[3] == check_list[3]:
			check_secret += 1

def my_remove(c):  # 제거되는 문자를 처리하는 함수

	global check_list, my_list, check_secret

	if c == 'A':
		if my_list[0] == check_list[0]:
			check_secret -= 1
		my_list[0] -= 1

	elif c == 'C':
		if my_list[1] == check_list[1]:
			check_secret -= 1
		my_list[1] -= 1

	elif c == 'G':
		if my_list[2] == check_list[2]:
			check_secret -= 1
		my_list[2] -= 1

	elif c == 'T':
		if my_list[3] == check_list[3]:
			check_secret -= 1
		my_list[3] -= 1

s, p = map(int, input().split())
result = 0
a = list(input())
check_list = list(map(int, input().split()))

for i in range(4):
	if check_list[i] == 0:
		check_secret += 1

for i in range(p):  # 초기 p 부분 문자열 처리 부분
	my_add(a[i])
	if check_secret == 4:  # 4 자릿수와 관련된 크기가 모두 충족될 때 유효한 비밀번호
		result += 1

for i in range(p, s):
	j = i - p
	my_add(a[i])
	my_remove(a[j])
	if check_secret == 4:
		result += 1

print(result)
