from threading import Thread, Lock

NUM_THREADS = 4

shared_counter = 0
shared_lock = Lock()

threads = []

def work():
    for _ in range(1000000):
        global shared_counter
        global shared_lock

        shared_lock.acquire()
        shared_counter += 1
        shared_lock.release()

for thread in range(NUM_THREADS):
    t = Thread(target=work, daemon=True)
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()
    print("Thread {} joined".format(thread))

print(shared_counter)
