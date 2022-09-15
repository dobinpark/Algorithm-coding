b = []

for i in range(10):
    a = int(input())
    b.append(a % 42)

b = set(b)  # 중복된 값 묶기
print(len(b))