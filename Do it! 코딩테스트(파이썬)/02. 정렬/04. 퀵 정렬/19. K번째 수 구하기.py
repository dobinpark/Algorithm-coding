import sys

input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))


def quick_sort(s, e, k):
	global a
	if s < e:
		pivot = partition(s, e)
		if pivot == k:   # K번째 수가 pivot이면 더는 구할 필요 없음
			return
		elif k < pivot:  # K가 pivot보다 작으면 왼쪽 그룹만 정렬
			quick_sort(s, pivot - 1, k)
		else:            # K가 pivot보다 크면 오른쪽 그룹만 정렬
			quick_sort(pivot + 1, e, k)


def swap(i, j):
	global a
	temp = a[i]
	a[i] = a[j]
	a[j] = temp


def partition(s, e):
	global a

	if s + 1 == e:
		if a[s] > a[e]:
			swap(s, e)
		return e

	m = (s + e) // 2
	swap(s, m)
	pivot = a[s]
	i = s + 1
	j = e

	while i <= j:
		while pivot < a[j] and j > 0:
			j = j - 1
		while pivot > a[i] and i < len(a) - 1:
			i = i + 1
		if i <= j:
			swap(i, j)
			i = i + 1
			j = j - 1
	# i == j 피벗의 값을 양쪽으로 분리한 가운데에 오도록 설정하기
	a[s] = a[j]
	a[j] = pivot
	return j


quick_sort(0, n - 1, k - 1)
print(a[k - 1])
