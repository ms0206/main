import time
from pathlib import Path
path_to_file = Path('C://Users/marius.sutkus.QDTEAM/Documents/training_2/measurements_100.txt')


def avr(par):
	return round(sum(par)/len(par),2)
time_start = time.time()
name_val = {}
name_val_calc = {}
with open(path_to_file, 'r') as file:
	for line in file:
		line = line.split(';')
		name_val.setdefault(line[0], [])
		name_val[line[0]].append(float(line[1][:-1]))
parsing_time = time.time() - time_start
for name, val in name_val.items():
	name_val_calc[name] = [min(val), avr(val), max(val)]
time_finish = time.time() - time_start
calculation_time = time_finish - parsing_time

print('finish_time: ', time_finish)
print('parsing_time', parsing_time)
print('calculation_time', calculation_time)

# print(name_val_calc)
# 10 000 000 time 8.796817064285278
# 100 000 000 time is 104.24603772163391
