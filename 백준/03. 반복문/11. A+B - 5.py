while True:
	a, b = map(int, input().split())
	if a + b > 0:
		print(a + b)
	elif a == 0 and b == 0:
		break
