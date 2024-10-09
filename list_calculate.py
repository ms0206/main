import time
import cProfile
import logging
import re
from pathlib import Path


def avg(par: float):
    return round(sum(par)/len(par),2)

def read_file_0(path_to_file: Path):
    pr_name = None
    val_list = []

    for line in sorted(path_to_file.read_text().splitlines()):
        name, val = line.split(';')
        
        if not pr_name:
            pr_name = name
            val_list.append(float(val))
        
        elif pr_name == name:
            val_list.append(float(val))
        
        else:
            print(f'{pr_name}: {[min(val_list), avg(val_list), max(val_list)]}')
            pr_name = name
            val_list = [float(val)]

def read_file_1(path_to_file: Path):
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    pr_name = None
    val_list = []

    for line in sorted(path_to_file.read_text().splitlines()):
        name, val = line.split(';')
        
        if not pr_name:
            pr_name = name
            val_list.append(float(val))
        
        elif pr_name == name:
            val_list.append(float(val))
        
        else:
            logging.debug(f'{pr_name}: {[min(val_list), avg(val_list), max(val_list)]}')
            pr_name = name
            val_list = [float(val)]

def read_file_2(path_to_file: Path):
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    pr_name = None
    val_list = []
    text = path_to_file.read_text().splitlines()
    for line in sorted(text):
        name, val = line.split(';')
        
        if not pr_name:
            pr_name = name
            val_list.append(float(val))
        
        elif pr_name == name:
            val_list.append(float(val))
        
        else:
            logging.debug(f'{pr_name}: {[min(val_list), avg(val_list), max(val_list)]}')
            pr_name = name
            val_list = [float(val)]




if __name__ == '__main__':

    time_start = time.time()
    path_to_file = Path('C://Users/marius.sutkus.QDTEAM/Documents/training_2/measurements_2.txt')

    read_file_2(path_to_file=path_to_file)
    # cProfile.run('read_file_0(path_to_file=path_to_file)')

    time_finish = time.time() - time_start

    print('finish_time: ', time_finish)

# read_file_0
# finish_time:  23.216512203216553
# [Finished in 23.4s]

# read_file_1
# finish_time:  22.941641092300415
# [Finished in 23.1s]
