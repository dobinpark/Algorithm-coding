arr = list(map(int, input().strip().split()))
arr2 = [1, 1, 2, 2, 2, 8]
print(" ".join(str(b - a) for a, b in zip(arr, arr2)))
