# TODO Найдите количество книг, которое можно разместить на дискете
B = 1024    # константы
KB = 1024
obem = 1.44     # Вводим данные
stranic = 100
strok = 50
simvol = 25
vessimvola = 4
perevod = B*KB
full = stranic * strok * simvol * vessimvola / perevod    # основной расчет
kolbook = int(obem // full)   # Делаем число целым
print("Количество книг, помещающихся на дискету:", kolbook)
