my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
len = len(my_list)
while 1 > 0:
    if index == len:
        break
    elif my_list[index] >= 1:
        print(my_list[index])
        index = index + 1
    elif my_list[index] == 0:
        index = index + 1
    else:
        break