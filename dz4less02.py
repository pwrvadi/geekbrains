# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
a = input("Введите предложение")
a = (a.split())
if len(str(a)) <= 10:
    for i, a in enumerate(a):
        print(i + 1, a)
else:
    for i, a in enumerate(a):
        print(i + 1, a[0:10])

