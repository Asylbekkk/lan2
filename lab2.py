#Asylbek
radius = int(input("радиус жаз "))

if radius >= 0:
    print("Длина окружности = ",  2  *  3.14  *  radius)
    print("Аудан = ", 3.14 * radius ** 2)
else:
    print("Пожалуйста, введите положительное число")