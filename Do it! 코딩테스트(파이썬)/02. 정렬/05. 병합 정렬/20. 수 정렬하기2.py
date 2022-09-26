import sys
input = sys.stdin.readline
print = sys.stdin.write

def merge_sort(s, e):  # 병합 정렬 수행
	if e - s < 1: return
	m = int(s + (e - s) / 2)
	merge_sort(s, m)
	merge_sort(m + 1, e)

	for i in range(s, e + 1):
		tmp[i] = a[i]

	k = s
	index1 = s
	index2 = m + 1

	while index1 <= m and index2 <= e:  # 두 그룹을 병합하는 로직
		if tmp[index1] > tmp[index2]:
			a[k] = tmp[index2]
			k += 1
			index2 += 1
		else:
			a[k] = tmp[index2]
			k += 1
			index1 += 1

	while index1 <= m:  # 한쪽 그룹이 모두 선택된 후 남아 있는 값 정리
		a[k] = tmp[index1]
		k += 1
		index1 += 1
	while index2 <= e:
		a[k] = tmp[index2]
		k += 1
		index2 += 1

n = int(input())
a = [0] * int(n + 1)
tmp = [0] * int(n + 1)

for i in range(1, n + 1):
	a[i] = int(input())

merge_sort(1, n)

for i in range(1, n + 1):
	print(str(a[i]) + '\n')
