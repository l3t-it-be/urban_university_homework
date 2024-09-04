def calculate_structure_sum(data):
    """
    Рекурсивная функция для подсчета суммы всех чисел и длин всех строк
    во вложенных структурах данных.
    """
    total_sum = 0

    # Внутренняя рекурсивная функция для обработки разных типов данных
    def recursive_sum(item):
        nonlocal total_sum
        if isinstance(item, int):  # Если элемент - число, добавляем его к сумме
            total_sum += item
        elif isinstance(item, str):  # Если элемент - строка, добавляем её длину к сумме
            total_sum += len(item)
        elif isinstance(
            item, (list, tuple, set)
        ):  # Если элемент - список, кортеж или множество, проходим по всем внутренним элементам
            for sub_item in item:
                recursive_sum(sub_item)
        elif isinstance(
            item, dict
        ):  # Если элемент - словарь, проходим по всем ключам и значениям
            for key, value in item.items():
                recursive_sum(key)
                recursive_sum(value)

    # Запускаем рекурсивную функцию
    recursive_sum(data)
    return total_sum


# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    'Hello',
    ((), [{(2, 'Urban', ('Urban2', 35))}]),
]

result = calculate_structure_sum(data_structure)
print(result)
