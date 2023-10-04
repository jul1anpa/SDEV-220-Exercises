import multiprocessing as mp
from multiprocessing import Process, Queue
import time
import random as r



def calc_time(delay, pos):
    start = time.time()
    time.sleep(delay)
    current = time.strftime('%H:%M:%S', time.localtime())
    end = time.time()
    proc_time = end - start
    print(f'Process {pos} returned the time {current} in {proc_time} seconds')

if __name__ == "__main__":
    mp.set_start_method('spawn')
    processes = []
    queue_pos = 1
    
    for i in range(3):
        p = Process(target=calc_time, args=(r.randint(1, 10), queue_pos))
        processes.append(p)
        p.start()
        queue_pos += 1

    for process in processes:
        p.join()