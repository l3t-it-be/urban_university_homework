def apply_all_func(int_list: list[int | float], *functions):
    return dict(map(lambda func: (func.__name__, func(int_list)), functions))


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
