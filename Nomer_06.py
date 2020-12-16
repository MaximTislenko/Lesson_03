def lat_func(word):
    lat_char = 'qwertyuiopasdfghjklzxcvbnm'
    return word.title() if not set(word).difference(lat_char) else False

words = input('введите строку из слов, разделенных пробелом: ').split()
for w in words:
    res = lat_func(w)
    if res:
        print(lat_func(w), ' ')