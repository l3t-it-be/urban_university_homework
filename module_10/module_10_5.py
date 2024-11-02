import time
import multiprocessing
import os
from tqdm import tqdm
import glob


def read_info(name):
    all_data = []
    try:
        with open(name, 'r', encoding='utf-8') as file:
            while line := file.readline():
                all_data.append(line)
    except FileNotFoundError:
        print(f'Файл {name} не найден.')
    except Exception as e:
        print(f'Ошибка при чтении файла {name}: {e}')
    return


if __name__ == '__main__':
    filenames = glob.glob('./Files/*.txt')

    for filename in filenames:
        if not os.path.exists(filename):
            print(f'Файл {filename} не найден!')

    start_time = time.time()
    for filename in tqdm(filenames, desc='Линейное чтение'):
        read_info(filename)
    end_time = time.time()
    print(f'Линейное чтение: {end_time - start_time:.6f} секунд')

    start_time = time.time()
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.map(read_info, tqdm(filenames, desc='Многопроцессное чтение'))
    end_time = time.time()
    print(f'Многопроцессное чтение: {end_time - start_time:.6f} секунд')
