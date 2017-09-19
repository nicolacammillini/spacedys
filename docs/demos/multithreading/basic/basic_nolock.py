from threading import Thread

NUM_THREADS = 4

shared_counter = 0

threads = []

def work():
    for i in range(1000000):
        global shared_counter
        shared_counter += 1

for thread in range(NUM_THREADS):
    t = Thread(target=work, daemon=True)
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()
    print("Thread {} joined".format(thread))

print(shared_counter)
