#1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
number = int(0b10001)
string = "stroka"
tuple_list = ('blue', 'red', 'green')
more = {1, 1, 1, 2, 2, 3, 4, 5}
krtmnj = frozenset(more)
new_dict = {"name": "Jenya", "age": 10, "address": "China"}
byte_string = b"hello world"
listdz1 = [number, string, tuple_list[0], more, krtmnj, new_dict.get("address"), byte_string]

print(listdz1)


print(type(number))
print(type(string))
print(type(tuple_list))
print(type(more))
print(type(krtmnj))
print(type(new_dict))
print(type(byte_string))
print(type(list))
