t = int(input())
for i in range(t):
    cnt, r = input().split()
    for j in r:
        print(j * int(cnt), end='')
    print()
