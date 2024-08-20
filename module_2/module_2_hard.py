def get_password(num):
    result = ''
    for i in range(1, num):
        for j in range(i, num + 1):
            if (i + j) % num == 0:
                result += str(i) + str(j)

    return result


n = int(input('Введите число от 3 до 20: '))
password = get_password(n)
print(f'Пароль для числа {n}: {password}')
