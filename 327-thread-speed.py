# Let us measure the time spend in two cases:
# 1) 10 tasks, 10 threads (max possible)
# 2) 10 tasks, 1 thread
from concurrent.futures \
    import ThreadPoolExecutor, as_completed
import time

def do_work(x):
    time.sleep(0.1)
    print(x)

n_tasks = 10 # number of tasks
n_threads = 10 # number of threads
# n_threads = 1 # number of threads
with ThreadPoolExecutor(max_workers=n_threads) as e:
    for x in range(n_tasks):
        e.submit(do_work, x)
