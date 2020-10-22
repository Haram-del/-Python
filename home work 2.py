#Первое задание

# Обявление списка

list = ["str", 3, 67, 56.5, b"bytes"]

#Проверка типов

for object in list:
    print(type(object))

#Третье задание

months = {
    1: "зима",
    2: "зима",
    3: "весна",
    4: "весна",
    5: "весна",
    6: "лето",
    7: "лето",
    8: "лето",
    9: "осень",
    10: "осень",
    11: "осень",
    12: "зима"
}
user_number = int(input("Введите цифру от 1 до 12"))
print(months[user_number])

#Четвертое задание

user_word = input("Ведите предложение: ")

word_fr = user_word.split(" ")

for word in word_fr:
    print(word[:10])

#Пятое задание


my_list = (7, 5, 3, 3,2)
new_number = 5
index = 0

for item in my_list:
    if new_number <= item:
        index = my_list.index(item) + 1

my_list.insert(index, new_number)