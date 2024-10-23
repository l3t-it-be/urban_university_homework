def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)

        if res < 2:
            print('Составное')
            return res

        for i in range(2, int(res**0.5) + 1):
            if res % i == 0:
                print('Составное')
                return res

        print('Простое')
        return res

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
