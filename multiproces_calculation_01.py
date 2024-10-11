import multiprocessing as mp
import sys
import time
from pathlib import Path
from typing import List, Dict


class DataNames:
    min_v = 'min_v'
    max_v = 'max_v'
    sum_v = 'sum_v'
    count_v = 'count'
    stop = 'stop'


def join_dicts(results: List[Dict]) -> Dict:
    result = results[0]

    if len(results) > 1:

        for elm in results[1:]:
            for name, value in elm.items():

                if not result.get(name):
                    result[name] = value

                else:
                    if result[name][DataNames.min_v] > value[DataNames.min_v]:
                        result[name][DataNames.min_v] = value[DataNames.min_v]

                    if result[name][DataNames.max_v] < value[DataNames.max_v]:
                        result[name][DataNames.max_v] = value[DataNames.max_v]

                    result[name][DataNames.sum_v] += value[DataNames.sum_v]
                    result[name][DataNames.count_v] += value[DataNames.count_v]

    return result


def print_data(name_val: Dict):

    for name, val in sorted(name_val.items()):
        print(f'{name}: '
              f'min: {val[DataNames.min_v]}, '
              f'max: {val[DataNames.max_v]}, '
              f'avg: {val[DataNames.sum_v]/val[DataNames.count_v]}')

    print(f'dict length: {len(name_val.keys())}')
    print(f'size of dict in bytes: {sys.getsizeof(name_val)}')


def run_data(inputs: mp.Queue, outputs: mp.Queue):

    name_val = {}

    while True:

        line = inputs.get()
        if line == 'Stop':
            break

        name, val = line.split(';')
        val = float(val)

        if name_val.get(name) is None:
            name_val[name] = {}
            name_val[name][DataNames.min_v] = val
            name_val[name][DataNames.max_v] = val
            name_val[name][DataNames.sum_v] = val
            name_val[name][DataNames.count_v] = 1

        else:
            name_val[name][DataNames.count_v] += 1
            name_val[name][DataNames.sum_v] += val

            if val < name_val[name][DataNames.min_v]:
                name_val[name][DataNames.min_v] = val

            elif val > name_val[name][DataNames.max_v]:
                name_val[name][DataNames.max_v] = val

    outputs.put(name_val)


def run_multi_proces(path_file: Path):
    t_start = time.time()
    input_queue = mp.Queue()
    result_queue = mp.Queue()
    process: List = []
    results: List = []
    result = None

    nr_pr = 2

    for i in range(nr_pr):
        prc = mp.Process(target=run_data, args=[input_queue, result_queue])
        prc.start()
        process.append(prc)

    with path_file.open() as file:
        count = 1
        for line in file:
            # if count % 1000 == 0:
            #     break

            input_queue.put(line)
            count += 1

    print('end of loop')
    print(time.time() - t_start)

    for i in process:
        print(f'stop input: {i=}')
        input_queue.put('Stop')

    for i, prc in enumerate(process):
        print('stop process')
        print(f'{i=}')
        prc.join()

    while not result_queue.empty():
        res = result_queue.get()
        results.append(res)
        print(f'length of result: {len(res)}')

    if results:
        result = join_dicts(results)

    if result:
        print_data(result)
    t_end = time.time() - t_start
    print(f'end of the function: {t_end}')

if __name__ == "__main__":

    path_to_file = Path('C://Users/marius.sutkus.QDTEAM/Documents/training_2/measurements_15.txt')
    run_multi_proces(path_file=path_to_file)

#  15M, 1 Proces
# dict len: 413
# size of dict: 13056
# 303.0186593532562

#  15M, 2 Proces
# dict length: 413
# size of dict in bytes: 13056
# end of the function: 462.93031191825867

# end of loop
# 32.49544072151184
# stop input
# stop run data
# this is outside function
# len of result: 413
# stop input
# stop run data
# this is outside function
# len of result: 413
# stop input
# stop run data
# this is outside function
# len of result: 413
# stop input
# stop run data
# this is outside function
# len of result: 413
# i=0
# stop process
# i=1
# stop process
# i=2
# stop process
# i=3
# stop process
# 515.6961214542389
