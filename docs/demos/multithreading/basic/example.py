import time
from threading import Thread

NUM_THREADS = 4

threads = []


class BasicThread(Thread):

    def __init__(self, message):
        super().__init__()
        self._message = message

    def run(self):
        for _ in range(10):
            time.sleep(1)
            print(self._message)


for thread in range(1, NUM_THREADS + 1):
    t = BasicThread("In thread {}".format(thread))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()
    print("Thread {} joined".format(thread))
