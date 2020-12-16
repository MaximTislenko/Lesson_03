def my_func(x, y, z):
    list = [x, y, z]
    x = sum(list) - min(list)
    return(x)
x = int(input('01-'))
y = int(input('02-'))
z = int(input('03-'))
print(my_func(x, y, z))