import multiprocessing as mp
import os
import time
from pathlib import Path


class DataContainer:
    name_val = {}


def avg(par: float):
    return round(sum(par) / len(par), 2)

def print_data(result):
    for name, val in sorted(result.items()):
        print(f'{name}: {[min(val), avg(val), max(val)]}')

def run_data(inputs: mp.Queue, outputs: mp.Queue):
    name_val = {}
    while True:
        line = inputs.get()
        print(line)
        if line == 'Stop':
            print('stop run data')
            # todo hangs when puting data
            outputs.put(name_val)
            break
        name, val = line.split(';')
        name_val.setdefault(name, []).append(float(val))
    print('this is outside function')


def run_multi_proces(path_file: Path):
    # t_start = time.time()

    input_queue = mp.Queue()
    result_queue = mp.Queue()
    process: list = []

    nr_pr = 4
    for i in range(nr_pr):
        prc = mp.Process(target=run_data, args=[input_queue, result_queue])
        prc.start()
        process.append(prc)
    t_start = time.time()

    with path_file.open() as file:
        for line in file:
            input_queue.put(line)

    # loop time is 27 s.
    print('end of loop')
    t_end = time.time() - t_start
    print(t_end)

    for _ in process:
        print('stop input')
        input_queue.put('Stop')

    for i, prc in enumerate(process):
        print(f'{i=}')
        print('stop process')
        prc.join()

    result = result_queue.get()
    print_data(result)
    t_end = time.time() - t_start
    print(t_end)


def run_multi_proces_01(path_file: Path):
    # t_start = time.time()

    input_queue = mp.Queue()
    result_queue = mp.Queue()
    process: list = []

    nr_pr = 4
    for i in range(nr_pr):
        prc = mp.Process(target=run_data, args=[input_queue, result_queue])
        prc.start()
        process.append(prc)
    t_start = time.time()

    with path_file.open() as file:
        for line in file:
            input_queue.put(line)

    # loop time is 27 s.
    print('end of loop')
    t_end = time.time() - t_start
    print(t_end)

    for _ in process:
        print('stop input')
        input_queue.put('Stop')

    for i, prc in enumerate(process):
        print(f'{i=}')
        print('stop process')
        prc.join()

    result = result_queue.get()
    print_data(result)
    t_end = time.time() - t_start
    print(t_end)


if __name__ == "__main__":
    path_to_file = Path('C://Users/marius.sutkus.QDTEAM/Documents/training_2/measurements_2.txt')
    run_multi_proces(path_file=path_to_file)

