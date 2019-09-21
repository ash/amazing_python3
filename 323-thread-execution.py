from concurrent.futures \
    import ThreadPoolExecutor, as_completed
import time

# Let's execute the following function
# "in parallel" (using threads):
def do_work(x):
    time.sleep(0.1)
    print(x)

jobs = []
n_jobs = 10 # number of threads
with ThreadPoolExecutor(max_workers=n_jobs) as e:
    for x in range(n_jobs):
        jobs.append(e.submit(do_work, x))
        # submit a job to execute a function
        # with an argument (x)
# All jobs submitted
# They will be executed in random order