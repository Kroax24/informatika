def find_index(items, target):   # Создаём функцию для поиска индекса
    for i in range(len(items)):  # Перебираем список по индексам
        if items[i] == target:   # Проверяем, равеняется ли текущий элемент нужному
            return i             # Если нашли, возвращаем индекс
    return None                  # Если не нашли

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list, find_item)   # Вызываем функцию и получаем индекс
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
     print(f"Товар '{find_item}' не найден в списке.")



