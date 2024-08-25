def print_params(a=3, b='default parameters', c=True):
    print(a, b, c)


print_params()
print_params(b='one non-default parameter')
print_params(a=(2 + 2), b='4')
print_params(a=20, b='= 20', c=False)

print_params(b=25)  # работает, но PyCharm ругается, что не тот тип данных
print_params(c=[1, 2, 3])  # работает, но PyCharm ругается, что не тот тип данных

values_list = ['values list', 3, (1, 2, 3)]
values_dict = {'a': 4, 'b': 'some string', 'c': True}

print_params(*values_list)
print_params(**values_dict)
# print_params(*values_list, **values_dict) - ошибка, т.к. значений больше, чем параметров

values_list_2 = [10, 'ten']
print_params(
    *values_list_2, 42
)  # работает, но PyCharm присваивает значение 42 параметру 'a', а не 'c'
