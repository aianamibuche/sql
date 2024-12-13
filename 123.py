# Задание 1
temp = 12
if temp < 0:
    print("Наденьте теплую куртку и шарф")
elif 0 <= temp <= 15:
    print("Наденьте легкую куртку")
else:
    print("Наденьте футболку и шорты")

# Задание 2
number = 15
if number % 3 == 0 and number % 5 == 0:
    print(f"Число {number} делится и на 3 и на 5")
elif number % 3 == 0:
    print(f"Число {number} делится на 3")
elif number % 5 == 0:
    print("Число делится на 5")
else:
    print(f"Число {number} не делится ни на 3, ни на 5")

# Задание 3
a, b, c = 5, 5, 9
if a == b == c:
    print("Равносторонний треугольник")
elif a == b or b == c or a == c:
    print("Равнобедренный треугольник")
else:
    print("Разносторонний треугольник")

# Задание 4
speed = 25
if speed < 10:
    print("Очень медленный интернет")
elif 10 <= speed <= 50:
    print("Средняя скорость интернета")
else:
    print("Высокая скорость интернета")

# Задание 5
money = 100
currency = "тенге"
if currency == "рубль":
    print("Сумма в рублях:", money * 75)
elif currency == "тенге":
    print("Сумма в тенге:", money * 470)
elif currency == "евро":
    print("Сумма в евро:", money * 0.85)
else:
    print("Неизвестная валюта")
