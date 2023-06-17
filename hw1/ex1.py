#Найдите сумму цифр трехзначного числа.

number = int(input('Введите трехзначное число '))
i=0
sum=0
if number<1000 and number>99:
    while i<3:
        sum+=number%10
        i+=1
        number//=10
    print('Сумма цифр числа равна: ', sum)
else:
    print('Число не трехзначное')