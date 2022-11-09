p, k = map(int, input().split())
count = 0

for i in range(k, p + 1):
    if p > k:
        count += 1
    elif p == k:
        break

print(count)
