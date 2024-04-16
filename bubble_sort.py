number_lst = list(map(int, input().split()))
number_lst = [4, 5, 2, 0, 6, 3, -56, 3, -1]
for elem in range(len(number_lst)-1):
    for el2 in range(len(number_lst)-1-elem):
        if number_lst[el2] > number_lst[el2+1]:
            number_lst[el2], number_lst[el2+1] = number_lst[el2+1], number_lst[el2]
print(*number_lst)
