import math

radius = float(input("Введіть радіус кола => "))
diameter = 2 * radius 
length = 2 * radius * math.pi
print("Коло з радіусом:" , radius , ", має діаметр:" , diameter , "та довжину:", round(length, 3) , "\n")

#============================================================#
sideA = float(input("Введіть сторону А => "))
sideB = float(input("Введіть сторону Б => "))
perimeter = sideA * 2 + sideB * 2 
diagonal = math.sqrt(sideA * sideA + sideB * sideB)
print("Прямокутник зі сторонами А:" , sideA , "і Б:" , sideB , ", має периметер:", perimeter , "та діагональ:", round(diagonal, 2) , "\n")

#============================================================#
n1 = int(input("Введіть ціле число: "))
n2 = 0
 
while n1 > 0:
    digit = n1 % 10
    n1 = n1 // 10
    n2 = n2 * 10
    n2 = n2 + digit  
 
print("Перевернуте число:" , n2 , "\n")

#============================================================#
x = float(input("Введіть точку Х => "))
y = float(input("Введіть точку У => "))

if (y <= -1 and y >= -2 and x >= 1 and x <= 3):
    print("Точка входить у виділену область!")
else:
        print("Точка не входить у виділену область!")