# a는 재산, 보험, 급여등 고정 비용
# b는 노트북을 생사하는 데 드는 재료비와 인건비 가변 비용
# c는 노트북 가격

a, b, c = map(int, input().split())

if b >= c:  # 손익분기점 존재x
	print(-1)
else:  # 손익분기점 존재
	print(int(a / (c - b) + 1))
