def plural_form(value, form1, form2, form5):
    n = abs(value) % 100
    print("Остаток от деления на 100 равен ", n)
    n1 = n % 10
    print("Остаток от деления на 10 равен ", n1)
    result_form = form5
    if 10 < n < 20:
        result_form = form5
    elif 1 < n1 < 5:
        result_form = form2
    elif n1 == 1:
        result_form = form1
    return f'{value} {result_form}'

print(plural_form(1, 'яблоко', 'яблока', 'яблок'))
print(plural_form(2, 'яблоко', 'яблока', 'яблок'))
print(plural_form(11, 'студент', 'студента', 'студентов'))
print(plural_form(15, 'студент', 'студента', 'студентов'))
print(plural_form(3, 'студент', 'студента', 'студентов'))

summ = 0
for i in range(1000, 20001):
    if i % 3 == 0 and i % 5 == 0:
        summ += i
print(f'Сумма чисел, которые делятся и на 3 и на 5 = {summ}')

def fibonacci_sequence(zero_step, first_step, threshold):
    next_step = 0
    list_of_numbers = [zero_step, first_step]
    while next_step < threshold:
        next_step = zero_step + first_step
        zero_step = first_step
        first_step = next_step
        if next_step < threshold:
            list_of_numbers.append(next_step)
    return(list_of_numbers)

fibonacci_list = fibonacci_sequence(1, 1, 10000000)

even_list = []
for number in fibonacci_list:
    if number % 2 == 0:
        even_list.append(number)

print(len(fibonacci_list))
print(sum(even_list))
print (even_list)
print(fibonacci_list[-2])



