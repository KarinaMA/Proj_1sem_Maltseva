# Даны целые числа a, b, c.
# Проверить истинность высказывания: "Существуют треугольник со сторонами a, b, c".

a = input("Введите первое целое число: ")
b = input("Введите второе целое число: ")
c = input("Введите третье целое число: ")

while type(a) != int:            # обработка исключений
    try:
        a = int(a)
    except ValueError:
        print("Ввели неправильное число")
        a = input("Введите первое целое число: ")
while type(b) != int:           # обработка исключений
    try:
        b = int(b)
    except ValueError:
        print("Ввели неправильное число")
        b = input("Введите второе целое число: ")
while type(c) != int:           # обработка исключений
    try:
        c = int(c)
    except ValueError:
        print("Ввели неправильное число")
        c = input("Введите третье целое число: ")

if((a + b) > c) and ((b + c) > a) and ((a + c) > b):
    print("True")
else:
    print("False")
