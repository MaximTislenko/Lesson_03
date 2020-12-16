def summa():
    res = 0
    while True:
        print(f"Текущая сумма = {res}")
        input_s = input("Введите строку чисел, разделенных пробелом(# - окончание): ").split()
        for val in input_s:
            if val == "#":
                print(f"Окончательная сумма = {res}")
                print('Пока!')
                break
            try:
                res += float(val)
            except ValueError:
                print(f"Значение {val} не было учтено, нужны цифры (арабские)")
        else:
            continue
        break
    return f"Окончательная сумма = {res}"


summa()