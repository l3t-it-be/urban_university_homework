def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


test_function()

# Попытка вызова inner_function вне test_function
# inner_function() # Вызовет ошибку NameError: name 'inner_function' is not defined
