# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.a = int(input("Введите месяц от 1 до 12"))
# Вариант через list
a = int(input("Напишите цифру месяца от 1 до 12"))
list = ["Это зима", "Это весна", "Это лето", "Это осень"]

if a == 12 or a == 1 or a == 2:
    print(list[0])
elif a == 3 or a == 4 or a == 5:
    print(list[1])
elif a == 6 or a == 7 or a == 8:
    print(list[2])
elif a == 9 or a == 10 or a == 11:
    print(list[3])
else:
    print("В году всего 12 месяцев")

# Вариант через dict
dict = {"Это зима": (12, 1, 2), "Это весна": (3, 4, 5), "Это лето": (6, 7, 8), "Это осень": (9, 10, 11)}
for key in dict.keys():
    if a in dict[key]:
        print(key)