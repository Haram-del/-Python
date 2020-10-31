#Первое задание
def calc():
    first_number = float(input('Введите количество отработанных часов : '))
    second_number = float(input('Введите суммы оплаты труда за 1 час : '))
    third = float(input('Укажите размер премии - '))
    pay = first_number * second_number
    return pay + third
print(f'Размер заработной платы составил: {calc() }')

#Второе задание

list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
for number in range(len(list) - 1):
    fun = [list[number]]
    number += 1
    fun_1 = [list[number]]
    if fun_1 > fun:
        fun_1 = fun
        print(fun_1, end='')

#Третье задание

for num in range(20,240):
    if num%20 ==0:
        print(num)

#Четвертое задание

hw_arr = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
four_arr =  [z for z in hw_arr if hw_arr.count(z) < 2]

print(four_arr)

#Пятое задание

five_arr = [c for c in range(100, 1001) if (c % 2) == 0]
sum_all = reduce(lambda x, y: x + y, five_arr)
print(sum_all)

#Седьмое задание

def gen(h):
    n = factorial(h)
    yield n

ready_test_arr = [d for d in gen(int(input("Факториал числа: ")))]
print(ready_test_arr)
