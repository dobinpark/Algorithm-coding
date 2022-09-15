n = int(input())
x = n
i = 0

while True:
    i += 1
    x = (x % 10) * 10 + ((x // 10) + (x % 10)) % 10
    if n == x:
        print(i)
        break
