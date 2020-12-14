def multiplication (x, y):
    return x / y
x = float(input("Введите первый множитель - "))
y = float(input("Введите второй множитель(он не должен быть равен 0) - " ))
while True:
    if y == 0:
        print("Второй множитель введен неправильно.")
        y = float(input("Повторите ввод второго множителя (он не должен быть равен 0) - "))
    if y != 0:
        break

print(f'{multiplication(x, y):.4f}')


