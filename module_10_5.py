from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file1:
        while True:
            line = file1.readline().strip()
            all_data.append(line)
            if not line:
                break

if __name__ == '__main__':
    files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

    start1 = datetime.now()
    for f in files:
        read_info(f)
    end1 = datetime.now()
    print(f'Линейный вызов: {end1 - start1}')

    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)
    end = datetime.now()
    print(f'Многопроцессный вызов: {end - start}')