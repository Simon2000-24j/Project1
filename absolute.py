def get_absolute_url(abs_url, *args, **kwargs):
    string_url = abs_url
    for arguments in args:
        string_url += '/' + arguments
    for k, v in kwargs.items():
        string_url += '?' + k + '=' + v + '&'
    #в строке последний знак получился "&" обрезаем его
    string_url = string_url[:-1]
    #в строке получились пары '&?', а должно быть '&' делаем замену шаблона для этих пар
    string_url = string_url.replace('&?', '&')
    return string_url


#ЭТО ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ.
#ЛИБО НАПИСАТЬ ВЫВОД ФУНКЦИЙ СО СВОИМИ ПАРАМЕТРАМИ
print(get_absolute_url('www.yandex.ru', 'posts', 'news', id='24', author='admin'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='azure', size='small'))
print(get_absolute_url('www.yandex.ru', 'posts', 'news', 'images', id='24', author='admin',  category='auto', color='azure', size='small'))
