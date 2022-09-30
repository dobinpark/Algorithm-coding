a, b = map(str, input().split())

a_list = list(a)
b_list = list(b)

a_index = int(a_list[2] + a_list[1] + a_list[0])
b_index = int(b_list[2] + b_list[1] + b_list[0])

print(max(a_index, b_index))
