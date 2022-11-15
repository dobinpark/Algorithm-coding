t = int(input())
count = 0

for i in range(1, t + 1):
    n = input()

    for j in range(1, 10):
        if n[:j] == n[j:j * 2]:
            print('#{} {}'.format(i, j))
            break
