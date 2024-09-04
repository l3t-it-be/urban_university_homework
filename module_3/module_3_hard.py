def calculate_structure_sum(data):
    """
    Рекурсивная функция для подсчета суммы всех чисел и длин всех строк
    во вложенных структурах данных.
    """
    if isinstance(data, int):  # Если элемент - число, возвращаем его значение
        return data
    elif isinstance(data, str):  # Если элемент - строка, возвращаем её длину
        return len(data)
    elif isinstance(
        data, (list, tuple, set)
    ):  # Если элемент - список, кортеж или множество, суммируем результаты для всех внутренних элементов
        return sum(calculate_structure_sum(sub_item) for sub_item in data)
    elif isinstance(
        data, dict
    ):  # Если элемент - словарь, суммируем результаты для всех ключей и значений
        return sum(
            calculate_structure_sum(key) + calculate_structure_sum(value)
            for key, value in data.items()
        )
    else:
        return 0  # Для остальных типов данных возвращаем 0


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
