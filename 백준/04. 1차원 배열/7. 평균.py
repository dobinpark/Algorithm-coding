n = int(input())
b = list(map(int, input().split()))

max = max(b)

for i in range(len(b)):
    b[i] = b[i] / max * 100

print(sum(b) / len(b))
