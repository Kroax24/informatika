participants_first_group = "Иванов|Петров|Сидоров"  # TODO Провеьте работу функции с разделителем отличным от запятой
participants_second_group = "Петров|Сидоров|Смирнов"


def find_common_participants(group1, group2, comma=','):  # Пишем функцию
    list1 = group1.split(comma)                           # Превращаем первую строку в список
    list2 = group2.split(comma)                           # Превращаем вторую строку в список
    common = []                                           # Создаем пустой список
    for name in list1:                                    # Запускаем цикл и прогоняем именя из первого списка
        if name in list2:                                 # Есть ли это имя во втором списке?
            if name not in common:                        # Есть ли дубликаты?
                common.append(name)                       # Добавляем имя
    common.sort()                                         # Сортируем в алфавитном порядке
    return common

print(find_common_participants(participants_first_group, participants_second_group, "|"))
