def get_value_from_list(object_list, separator, key):
    """Функция находит значение ключа key из списка object_list
    по разделителю separator
    :param object_list: список строк
    :param separator: разделитель
    :param key: искомый ключ"""

    # Объявляем переменную для хранения найденного значения
    value = None
    for element in object_list:
        # Итерируемся по каждому элементу из переданного списка object_list.
        # Каждый элемент разделяем на части, используя разделитель separator. 
        # В итоге получим, что первый элемент - это ключ, второй элемент - это значение.
        words = element.split(separator)
        if words[0] == key:
            # Если первый элемент равен искому ключу key, то обновляем значение value и выходим из цикла
            value = words[1]
            break
    
    # Возвращаем найденное значение
    return value
    

# Журнал регистрации
log = """name:Иван;gender:m;item:Часы;item_cost:9800
name:Иван;gender:m;item:Фитнес-браслет;item_cost:12300
name:Иван;gender:m;item:Кофемашина;item_cost:23500
name:Петр;gender:m;item:Часы;item_cost:9800
name:Петр;gender:m;item:Фитнес-браслет;item_cost:12300
name:Петр;gender:m;item:Айфон;item_cost:77900
name:Петр;gender:m;item:Чехол для телефона;item_cost:350
name:Петр;gender:m;item:Кофемашина;item_cost:23500
name:Дарья;gender:f;item:Айфон;item_cost:77900
name:Марья;gender:f;item:Кофемашина;item_cost:23500
name:Юлия;gender:f;item:Фитнес-браслет;item_cost:12300"""

log_13 = """name:Иван;gender:m;item:Часы;item_cost:9800
name:Иван;gender:m;item:Фитнес-браслет;item_cost:12300
name:Петр;gender:m;item:Часы;item_cost:9800
name:Петр;gender:m;item:Фитнес-браслет;item_cost:12300
name:Петр;gender:m;item:Чехол для телефона;item_cost:350
name:Юлия;gender:f;item:Фитнес-браслет;item_cost:12300"""

# Создаем итоговый список, в котором будем хранить разделенные записи
log_list = []
log_list_13 = []

# Делим журнал регистрации log на список строк по разделителю - перенос строки.
# Полученный результат сохраняем в список records
records = log.split('\n')
records_13 = log_13.split('\n')

for log_record_13 in records_13:
    
    record_dict_13 = {
        'name': '',
        'gender': '',
        'item': '',
        'item_cost': 0,
    }

    elements_13 = log_record_13.split(';')

    user_name_13 = get_value_from_list(elements_13, ':', 'name')
    user_gender_13 = get_value_from_list(elements_13, ':', 'gender')
    item_title_13 = get_value_from_list(elements_13, ':', 'item')
    item_cost_13 = get_value_from_list(elements_13, ':', 'item_cost')

    record_dict_13['name'] = user_name_13
    record_dict_13['gender'] = user_gender_13
    record_dict_13['item'] = item_title_13
    record_dict_13['item_cost'] = item_cost_13

    log_list_13.append(record_dict_13)



# Выводим итоговый список log_list_13
print(log_list_13)

