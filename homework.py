#   Первое задание

Number_One = 355
Number_Two = 567

print(Number_One + Number_Two)
print(Number_Two)
User_Number = int(input("Ведите число: "))
User_Str = (input("Ведите строку: "))
print(User_Number)
print(User_Str)

#   Второе задание
User_Number = int(input("Введите Время: "))

Hour = User_Number // 60 // 60
Min = User_Number // 60
Sec = User_Number % 60
if len(str(Hour)) < 2:
    Hour = "0" + str(Hour)
if len(str(Min)) < 2:
    Min = "0" + str(Min)
if len(str(Sec)) < 2:
    Sec = "0" + str(Sec)
print("{}:{}:{}".format(Hour, Min, Sec))

#   Третье задание

N = int(input("Ведите число: "))

print(N + N * 11 + N * 111)

#   Четвертое задание

number = int(input("Введите число: "))
max = 0
while number > 0:
    num = number % 10
    if num > max:
        max = num
    number //= 10
print(max)

#   Пятое задание

rev = int(input("Выручка: "))
cost = int(input("Издержки: "))
prof = rev - cost

try:
    part = rev / prof
except:
    print("Ушли в ноль")

if prof > 0:
    print("Прибыль ровна{}руб".format(prof))
    print("Часть выручки {}".format(round(part, 2)))
    staff = int(input("Количество сотрудников: "))
    print(prof // staff, " Руб сотруднику")
elif prof < 0
    print("В убытке")

    # Шестое задание

first = int(input("Первый день: "))
result = int(input("Результат: "))
day = 1

if first > result:
    print("Неверно")

while first <= result:
    print("{}день: {}км".format(day, round(first, 2)))
    day += 1
    result *= 1.10
print("На {} день спортсмен пробежал {}км".format(day, result))