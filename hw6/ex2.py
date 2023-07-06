# Задача 32: Определить индексы элементов массива (списка), значения 
# которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
list=[random.randint(1,10) for _ in range(10)]
print(list)
resultList=[]
minD=int(input('min '))
maxD=int(input('max '))
for i in range(len(list)):
    if minD<=list[i]<=maxD:
        resultList.append(i)
print(resultList)