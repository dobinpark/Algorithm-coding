n = input()
my_list = list(map(int, input().split()))
my_max = max(my_list)
sum = sum(my_list)

# 한 과목과 관련된 수식을 총합한 후 관련 수식으로 변환하여 로직을 간단하게 할 수 있음.
print(sum * 100 / my_max / int(n))
