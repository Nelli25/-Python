""" Пользователь вводит время в секундах.
Переведите время в часы,минуты,секунды и выведите в формате чч:мм:сс.
 Используйте форматирование строк """
time = int(input("Введите время в секундах: "))
hour = time // 3600
minuts = (time - (hour * 3600)) // 60
second = (time - (hour * 3600)) - (minuts * 60)
print(hour, ":", minuts, ":", second)
