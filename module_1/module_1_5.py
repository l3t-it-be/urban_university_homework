immutable_var = (
    'Python',
    42,
    True,
    ['Selenium', 'Selenide', 'Selene', 'Robot Framework'],
)
print(immutable_var)

'''
Элементы кортежа нельзя изменить, потому что кортеж - это неизменяемый тип данных
immutable_var[0] = 'Java' - выдаст ошибку

Но если внутри кортежа есть изменяемый тип данных, например список, 
то его элементы изменить можно
'''
immutable_var[3].remove('Robot Framework')
print(immutable_var)
immutable_var[3].append('Playwright')
print(immutable_var)


mutable_list = ['Python', 'Java', 'JavaScript', 'Go']
mutable_list[2] = 'TypeScript'
print(mutable_list)
