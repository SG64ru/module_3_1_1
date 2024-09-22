calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    string = input("Введите слово - ")                              #Ввод строки
    l_str = len(string)                                             # Подсчет кол-ва символов строки
    up_string = string.upper()                                      # Перевод символов строки в верхний регистр
    dow_string = string.lower()                                     # Перевод символов строки в нижний регистр
    print(l_str, up_string, dow_string)                             # Вывод на печать кортежа: Кол-ва символов, верхнем и нижнем регистре
    global calls                                                    # Объявление переменной - глобальной
    count_calls()                                                   # Вызов функции счетчика
    return count_calls()
    calls = count_calls()

    pass
string_info("string")

def is_contains(string, list_to_search):
    global calls
    string = input("Введите строку - ")
    list_to_search = input("Введите список - ")
    print(string in list_to_search)
    global calls  # Объявление переменной - глобальной
    count_calls()  # Вызов функции счетчика
    return count_calls()
    calls = count_calls()
    print(calls)
    count_calls()
    pass
is_contains("string", "list_to_search")
print(calls)


