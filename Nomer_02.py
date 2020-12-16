def passport (dict):
    for key in dict:
        val = input (key)
        dict[key] = val
    print(dict)

dict_01 = {"Имя" : [], "Фамилия" : [], "Год рождения" : [], "Город проживания" : [], "EMail" : [], "Телефон" : []}
passport (dict_01)

