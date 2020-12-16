def sec_func(x,y):
    i = 1
    for _ in range(abs(y)):
        x *= x
        i /= x
        return (i)  #Я не понимаю почему она не работает

def my_func(x, y):
    x= x**y
    return(x)
x = int(input('01-'))
y = int(input('02-'))
print(sec_func(x, y))
print(my_func(x, y))

