# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
n=int(input('введите количество элементов первого множества '))
m=int(input('введите количество элементов второго множества '))
set1=set()
set2=set()
for i in range(n):
    element1=int(input('введите элементы мн-ва 1 '))
    set1.add(element1)
for i in range(m):
    element2=int(input('введите элементы мн-ва 2 '))
    set2.add(element2)
print(sorted(set1.intersection(set2)))


