my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
nul = 0
while nul < len(my_list):
    if my_list[nul] < 0:
        break
    if my_list[nul] == 0:
        nul += 1

    print(my_list[nul])

    nul += 1
