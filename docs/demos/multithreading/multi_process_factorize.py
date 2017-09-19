from time import time

from multiprocessing import Process

def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i

def collect_factors(number):
    list(factorize(number))

numbers = [2139079, 1214759, 1516637, 1852285, 7834682, 34234223, 22087259, 6554269, 3675475, 7685843]

start = time()

processes = []

for number in numbers:
    process = Process(target=collect_factors, args=(number,))
    process.start()
    processes.append(process)
    

for process in processes:
    process.join()

end = time()

print('Took %.3f seconds' % (end - start))
