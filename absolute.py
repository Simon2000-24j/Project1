def get_absolute_url(num1, *args):
    print(args)
    for number in args:
        print(number)

get_absolute_url(2, 5, 6, 7)

# или

def get_absolute_url(num1, **kwargs):
    for k, v in kwargs.items():
        print(k, v)


get_absolute_url(2, a = 5, b = 6, c = 7)