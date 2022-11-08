t = int(input())
n = list(map(int, input().split()))

n.sort()
print(n[int((t - 1) / 2)])
