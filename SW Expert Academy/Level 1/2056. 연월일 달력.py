t = int(input())

for i in range(1, t + 1):
	n = input()

	year = n[:4]
	month = n[4:6]
	day = n[6:8]
	day_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
				7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

	if (int(month) >= 13) or (int(month) <= 0):
		print('#' + str(i), -1)
		continue
	else:
		if day_dict[int(month)] < int(day) or int(day) <= 0:
			print('#' + str(i), -1)
			continue
		else:
			print('#' + str(i), year +'/' + month + '/' + day)
