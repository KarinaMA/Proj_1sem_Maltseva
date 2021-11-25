# Описать функцию InvertDigits(K), меняющую порядок следования цифр целого положительного числа К на обратный
# (К-параметр целого типа, являющийся одновременно входным и выходным).
# С помощью этой функции поменять порядок следования цифр на обратный для каждого из пяти данных целых чисел.

def invert(k):                          # задание функции
    b = 0
    while k > 0:
        digit = k % 10
        k = k // 10
        b = b * 10 + digit
    return b


k = int(input("Введите число: "))
print("Обратное число: ", invert(k))
