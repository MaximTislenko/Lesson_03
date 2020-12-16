def summ_max():
    res_list = []
    while True:
        input_s = input ("Введите строку чисел, разделенных пробелом,(# - окончание): ").split()
        for val in input_s:
            if val == "#":
                print("Пока!")
                break
            else:
                res_list.append(int(val))
                break

    print(res_list)

summ_max()
