consumed = float(input("Введите количество потребленных кВт/ч: "))

if consumed <= 250:
    payment = consumed * 7
elif 250 < consumed <= 300:
    payment = 250 * 7 + (consumed - 250) * 17
else:
    payment = 250 * 7 + 50 * 17 + (consumed - 300) * 20

print("Плата за потребленные кВт/ч составляет:", payment, "руб.")