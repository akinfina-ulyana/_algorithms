def sum_array(list):
    if list == []:
        return 0
    return list[0]+sum_array(list[1:])
