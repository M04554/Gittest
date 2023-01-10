import time
from time import perf_counter
start=perf_counter()
def do_something():
    print('sleep one second')
    print('sleep one second 1')
    print('sleep one second 2')
    time.sleep(1)

do_something()
finish=pref_counter()
print(f'Finished in round{(finish-start,2)} second()')