def generate_password(num):
    result = ''

    for i in range(1, num):
        for j in range(i + 1, num + 1):
            pair_sum = i + j
            if num % pair_sum == 0:
                result += f'{i}{j}'

    return result


n = int(input('Введите число от 3 до 20: '))
if 3 <= n <= 20:
    password = generate_password(n)
    print(f'Нужный пароль для {n}: {password}')
else:
    print('Число должно быть в диапазоне от 3 до 20')
