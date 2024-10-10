import time
import cProfile
import logging
import re
from pathlib import Path


def avg(par: float):
    return sum(par)/len(par)

def print_data(name_val: dict):

    for name, val in sorted(name_val.items()):
        print(f'{name}: {[min(val), avg(val), max(val)]}')


def print_data_01(name_val: dict):


    for name, val in sorted(name_val.items()):
        val_f = [float(elm) for elm in val]
        print(f'{name}: {[min(val_f), avg(val_f), max(val_f)]}')


def print_data_02(name_val: dict):
    min_v = 'min_v'
    max_v = 'max_v'
    sum_v = 'sum_v'
    count = 'count'
    for name, val in sorted(name_val.items()):
        print(f'{name}: min: {val[min_v]}, max: {val[max_v]}, avg: {val[sum_v]/val[count]}')


def logging_data(name_val: dict):
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    for name, val in sorted(name_val.items()):
        logging.debug(f'{name}: {[min(val), avg(val), max(val)]}')


def read_file_0(path_to_file: Path):
    name_val = {}

    with path_to_file.open() as file:
        for line in file:
            name, val = line.split(';')

            name_val.setdefault(name, []).append(float(val))
    
    return name_val

def read_file_1(path_to_file: Path):
    name_val = {}

    with path_to_file.open() as file:
        for line in file:
            name, val = line.split(';')
            try:
                name_val[name].append(float(val))
            except KeyError:
                name_val[name] = [float(val)]
    return name_val

def read_file_2(path_to_file: Path):
    name_val = {}

    with path_to_file.open() as file:
        for line in file:
            name, val = line.split(';')
            if name_val.get(name) is None:
                name_val[name] = [float(val)]
            else:
                name_val[name].append(float(val))
            
    return name_val



def read_file_3(path_to_file: Path):
    name_val = {}

    with path_to_file.open() as file:
        for line in file:
            name = re.findall(r'(.*)\;', line)[0]
            val = float(re.findall(r'\;(.*)', line)[0])
            if name_val.get(name) is None:
                name_val[name] = [float(val)]
            else:
                name_val[name].append(float(val))
    return name_val


def read_file_4(path_to_file: Path):
    name_val = {}

    for line in sorted(path_to_file.read_text().splitlines()):
        name, val = line.split(';')
        
        if name_val.get(name) is None:
            name_val[name] = [float(val)]
        else:
            name_val[name].append(float(val))
            
    return name_val

def read_file_5(path_to_file: Path):
    name_val = {}

    for line in path_to_file.read_text().splitlines():
        name, val = line.split(';')
        
        if name_val.get(name) is None:
            name_val[name] = [float(val)]
        else:
            name_val[name].append(float(val))
            
    return name_val


def read_file_6(path_to_file: Path):
    name_val = {}

    with path_to_file.open() as file:
        for line in file:
            name, val = line.split(';')
            if name_val.get(name) is None:
                name_val[name] = [val]
            else:
                name_val[name].append(val)

def read_file_7(path_to_file: Path):
    min_v = 'min_v'
    max_v = 'max_v'
    sum_v = 'sum_v'
    count = 'count'
    name_val = {}

    with path_to_file.open() as file:
        for line in file:
            name, val = line.split(';')
            val = float(val)

            if name_val.get(name) is None:
                name_val[name] = {}
                name_val[name][min_v] = val
                name_val[name][max_v] = val
                name_val[name][sum_v] = val
                name_val[name][count] = 1

            else:
                name_val[name][count] += 1
                name_val[name][sum_v] += val
                if val < name_val[name][min_v]:
                    name_val[name][min_v] = val
                elif val > name_val[name][max_v]:
                    name_val[name][max_v] = val
    return name_val

if __name__ == '__main__':

    time_start = time.time()
    path_to_file = Path('C://Users/marius.sutkus.QDTEAM/Documents/training_2/measurements_100.txt')

    name_val = read_file_7(path_to_file=path_to_file)
    # name_val = cProfile.run('read_file_2(path_to_file=path_to_file)')

    read_time = time.time() - time_start
    if name_val:
        print_data_02(name_val)
    # logging_data(name_val)
    # print(name_val)
    time_finish = time.time() - time_start
    print_time = time_finish - read_time

    print('finish_time: ', time_finish)
    print('parsing_time', read_time)
    print('printing_time', print_time)

# read_file_2, logging
# finish_time:  11.324811697006226
# parsing_time 9.301223039627075
# printing_time 2.0235886573791504

# read_file_2, printing
# finish_time:  11.589313268661499
# parsing_time 9.629272937774658
# printing_time 1.9600403308868408

# read_file_1, printing
# finish_time:  10.838453769683838
# parsing_time 8.90363097190857
# printing_time 1.9348227977752686
# [Finished in 12.3s]

# read_file_0, printing
# finish_time:  10.84638237953186
# parsing_time 8.816593885421753
# printing_time 2.0297884941101074
# [Finished in 12.2s]

# read_file_3, printing
# finish_time:  33.37413930892944
# parsing_time 31.332564115524292
# printing_time 2.0415751934051514
# [Finished in 35.0s]

# read_file_4, printing
# finish_time:  23.236979722976685
# parsing_time 22.77725386619568
# printing_time 0.45972585678100586
# [Finished in 23.7s]

# read_file_5, printing
# finish_time:  10.722219705581665
# parsing_time 8.488081932067871
# printing_time 2.234137773513794
# [Finished in 12.2s]

# read_file_6, printing_01
# finish_time:  10.699799537658691
# parsing_time 5.829745054244995
# printing_time 4.870054483413696


# amount fo cities: 413
# all val: 15000000
# avg val per citie: 36319.61259079903

# read_file_7, printing_02
# finish_time:  12.291387796401978
# parsing_time 12.286099433898926
# printing_time 0.005288362503051758


# read_file_7, printing_02 100M
# finish_time:  88.19256091117859
# parsing_time 88.1845805644989
# printing_time 0.0079803466796875

# read_file_5, printing 100M
# finish_time:  118.19615459442139
# parsing_time 102.68240690231323
# printing_time 15.513747692108154

# read_file_0, printing 100M
# finish_time:  74.06772112846375
# parsing_time 59.81651163101196
# printing_time 14.251209497451782

# read_file_2, printing 100M
# finish_time:  75.28374767303467
# parsing_time 60.41977286338806
# printing_time 14.863974809646606
