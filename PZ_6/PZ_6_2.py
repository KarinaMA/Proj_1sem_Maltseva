# Дан целочисленный список A размера N (<15).
# Переписать в новый целочисленный список B все элементы с нечетными порядковыми номерами (1,3,...)
# и вывести размер полученного списка B и его содержимое.

import random

N=int(input("Введите размер списка A (< 15): "))
A=[]   #Создание списка
t=0
B=[]   #Создание списка

while t < N:
    A.append(random.randint(-100,100))   #Создание элементов списка
    t += 1
print(A)
for i in range (2):
    while i % 2 != 0 and i < N:
        B.append(A[i])
        i += 2
print (B)