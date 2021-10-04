import math

print("Введите коэффициенты для уравнения")
a = float(input("Напишите значение a:"))
b = float(input("Напишите значение b:"))
c = float(input("Напишите значение c:"))

D = b ** 2 - 4 * a * c
if D>0:
    x1 = (-b + D ** -0.5) / (2 * a)
    x2 = (-b - D ** -0.5) / (2 * a)
    print("x1 равно " + str(x1) + " и x2 равно " + str(x2))
elif D == 0:
    x = -b/ (2 * a)
    print("x равно " + str(x))
else:
    print("Корней нет")