from time import time

from threading import Thread

from subprocess import call

def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i

def collect_factors(number):
    list(factorize(number))

class FactorizeThread(Thread):

    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        call(["./factorize", str(self.number)])

numbers = [2139079, 1214759, 1516637, 1852285, 7834682, 34234223, 22087259, 6554269, 3675475, 7685843]

start = time()

threads = []

for number in numbers:
    thread = FactorizeThread(number)
    thread.daemon = True
    thread.start()
    threads.append(thread)
    

for thread in threads:
    thread.join()

end = time()

print('Took %.3f seconds' % (end - start))
