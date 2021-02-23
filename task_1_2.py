num = int(input('Введите кол-во секунд'))
sec = num % 60
min = (num // 60) % 60
hours = num // 3600
print(f'{hours} час  {min} мин {sec} сек')