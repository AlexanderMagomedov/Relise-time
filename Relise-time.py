from datetime import datetime
''' Команда BEEGEEK планирует выпустить свой новый курс 08.11.2022 ровно в 12:00. Напишите программу, которая принимает на вход текущие дату и время и определяет, сколько времени осталось до выхода курса.
'''
def choose_plural(amount,declensions):
    if int(amount) % 100 in range(21,100,10) or int(amount) % 100 == 1:
        return(str(amount)+' '+declensions[0])
    elif int(amount) % 100 in range(22,100,10) or int(amount) % 100 in range(23,100,10) or int(amount) % 100 in range(24,100,10) or int(amount) % 100 == 2 or int(amount) % 100 == 3 or int(amount) % 100 == 4 :
        return(str(amount)+' '+declensions[1])
    else:
        return(str(amount)+' '+declensions[2])

find_day = datetime(2022, 11, 8, 12) - datetime.strptime(input('Введите дату в формате dd.mm.yyy hh:mm '), '%d.%m.%Y %H:%M') #Тут можно сменить дату релиза.

if find_day.days < 0 or (find_day.days == 0 and find_day.seconds == 0):
    print('Курс уже вышел!')
elif find_day.days >= 1:
    if find_day.seconds // 3600 == 0:
        print(f'До выхода курса осталось: {choose_plural(find_day.days, ("день", "дня", "дней"))}')
    else:
        print(f'До выхода курса осталось: {choose_plural(find_day.days, ("день", "дня", "дней"))} и {choose_plural(find_day.seconds // 3600, ("час", "часа", "часов"))}')
else:
    if (find_day.seconds % 3600) // 60 == 0:
        print(f'До выхода курса осталось: {choose_plural(find_day.seconds // 3600, ("час", "часа", "часов"))}')
    elif find_day.seconds//3600 == 0:
        print(f'До выхода курса осталось: {choose_plural((find_day.seconds % 3600)//60,("минута", "минуты", "минут"))}')
    else:
        print(f'До выхода курса осталось: {choose_plural(find_day.seconds//3600,("час", "часа", "часов"))} и {choose_plural((find_day.seconds % 3600)//60,("минута", "минуты", "минут"))}')