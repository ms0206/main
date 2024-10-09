import time
from queue import Queue
from threading import Thread, Event


def pr_data(n: int) -> str:
    out = ''
    for i in range(n):
        out += f'{i=};'
    time.sleep(0.001)
    return out


def run_multi_data(inputs: Queue, result: Queue, work: Queue):
    while True:
        elm = inputs.get()
        res = pr_data(elm)
        result.put(res)
        if work.get() == 'Stop':
            break


def run_data():
    t_start = time.time()
    inputs = range(200)
    result = []
    for i, elm in enumerate(inputs):
        result.append(pr_data(elm))
    t_end = time.time() - t_start
    print(result[-1])
    print(t_end)


def run_multi_proces():
    t_start = time.time()
    # tr_event = Event()
    result_queue = Queue()
    input_queue = Queue()
    work_queue = Queue()
    work_queue.put('Start')
    threads: list = []

    inputs = range(201)
    nr_tr = 4
    # chunk_size = len(inputs) // nr_tr
    for _ in range(nr_tr):
        # print(i)
        # start = i * chunk_size
        # end = (i + 1) * chunk_size
        # if i == nr_tr - 1:
        #     end = len(inputs)
        #
        # data = inputs[start: end]

        trd = Thread(target=run_multi_data, args=[input_queue, result_queue, work_queue], daemon=True)
        trd.start()
        threads.append(trd)
    for i in inputs:
        input_queue.put(i)
    time.sleep(1)
    for trd in threads:
        work_queue.put('Stop')
        print(f'join thred: {trd}')
        trd.join()
    result = []
    while not result_queue.empty():
        res = result_queue.get()
        result.append(res)
    for trd in threads:
        work_queue.put('Stop')
        print(f'join thred: {trd}')
        trd.join()
    t_end = time.time() - t_start
    print(result)
    print(t_end)


if __name__ == "__main__":
    run_multi_proces()
    # run_data()
