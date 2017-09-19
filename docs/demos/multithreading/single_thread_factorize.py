from time import time

def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i

numbers = [2139079, 1214759, 1516637, 1852285, 7834682, 34234223, 22087259, 6554269, 3675475, 7685843]

start = time()

for number in numbers:
    print(list(factorize(number)))

end = time()

print('Took %.3f seconds' % (end - start))
