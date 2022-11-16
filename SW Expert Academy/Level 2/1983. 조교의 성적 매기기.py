t = int(input())

for i in range(1, t + 1):
	n, k = map(int, input().split(' '))
	students = []
	grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

	for j in range(n):
		a, b, c = map(int, input().split())
		sum_student = a * 0.35 + b * 0.45 + c * 0.20
		students.append(sum_student)

	k_score = students[k - 1]
	students.sort(reverse=True)

	rank_of_ten = students.index(k_score) // (n // 10) # 핵심 코드
	k_grade = grade[rank_of_ten]

	print('#' + str(i), k_grade)
