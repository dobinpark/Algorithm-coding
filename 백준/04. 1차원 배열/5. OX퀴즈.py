b = []

for k in range(int(input())):
    a = input()
    cut = 0
    score = 0

    for i in a:
        if i == 'O':
            cut += 1
            score += cut

        elif i == 'X':
            cut = 0

    b.append(score)

for i in b:
    print(i)
	