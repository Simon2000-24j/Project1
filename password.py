psw = input("Введите пароль: ")

try:
    temp = 25/len(psw)
    temp = int(psw)
    print("Ваш пароль состоит только из цифр.")
except ZeroDivisionError:
    print("Пустой пароль.")
except ValueError:
    print("Требования соблюдены.")
