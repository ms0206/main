import multiprocessing as mp
import os
import time
from pathlib import Path


def avg(par: float):
    return round(sum(par)/len(par),2)

def print_data(name_val: dict):

    for name, val in sorted(name_val.items()):
        print(f'{name}: {[min(val), avg(val), max(val)]}')

# def pr_data(n: int) -> str:
#     out = ''
#     for i in range(n):
#         out += f'{i=};'
#     time.sleep(0.001)
#
#     return out


def run_data(inputs: mp.Queue, result: mp.Queue):
    name_val = {}
    while True:
        line = inputs.get()
        name, val = line.split(';')
        name_val.setdefault(name, []).append(float(val))
        # todo
        result.put(name_val)


def run_multi_proces(path_file: Path):
    t_start = time.time()

    input_queue = mp.Queue()
    result_queue = mp.Queue()
    work_queue = mp.Queue()
    process: list = []

    nr_pr = 4
    for i in range(nr_pr):
        prc = mp.Process(target=run_data, args=[input_queue, result_queue])
        prc.start()
        process.append(prc)
    with path_file.open() as file:
        for line in file:
            input_queue.put(line)


    for prc in process:
        prc.join()
    result = []
    # while not result_queue.empty():
    res = result_queue.get()
    print_data(res)
    t_end = time.time() - t_start
    # print(result)
    # print(t_end)


if __name__ =="__main__":
    path_to_file = Path('C://Users/marius.sutkus.QDTEAM/Documents/training_2/measurements_15.txt')
    run_multi_proces(path_file=path_to_file)


