h, m = map(int, input().split())
time = int(input())

if m + time < 60:
	print(h, m + time)
elif m + time >= 60:
	if h + ((m + time) // 60) >= 24:
		print(h + ((m + time) // 60) - 24, (m + time - 60) % 60)
	elif h + ((m + time) // 60) < 24:
		print(h + ((m + time) // 60), (m + time - 60) % 60)
