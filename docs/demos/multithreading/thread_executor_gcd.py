from time import time
from concurrent.futures import ThreadPoolExecutor

def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

numbers = [(196330921, 226597312), (203067723, 381417214), (155164525, 222962056), (203904547, 202080248)]

start = time()

pool = ThreadPoolExecutor(max_workers = 4)

results = list(pool.map(gcd, numbers))

end = time()

print('Took %.3f seconds' % (end - start))
