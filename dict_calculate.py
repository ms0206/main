import time
import cProfile
import logging
import re
from pathlib import Path


def avg(par: float):
	return round(sum(par)/len(par),2)

def print_data(name_val: dict):

	for name, val in sorted(name_val.items()):
		print(f'{name}: {[min(val), avg(val), max(val)]}')

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


if __name__ == '__main__':

	time_start = time.time()
	path_to_file = Path('C://Users/marius.sutkus.QDTEAM/Documents/training_2/measurements_15.txt')

	name_val = read_file_4(path_to_file=path_to_file)
	# name_val = cProfile.run('read_file_2(path_to_file=path_to_file)')

	read_time = time.time() - time_start
	if name_val:
		print_data(name_val)
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