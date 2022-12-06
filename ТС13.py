import threading
from time import sleep
from time import time
import random
import logging


logging.basicConfig(level=logging.DEBUG)



lock = threading.Lock()
start = time()


def log(message: str):
    t = time() - start
    name = threading.current_thread().getName()
    logging.debug("[%6.3f] %s: %s", t, name, message)


def poizd(transit_time, arrive_time):
    sleep(arrive_time)
    log("прибув")
    with lock:
        log(f"рушив")
        sleep(transit_time)
    log("пройшов")
    print(f"{threading.current_thread().getName()} пройшов the sector.")


if __name__ == "main":
    n = 21
    t1 = 3
    t2 = 1
    t3 = 0
    t4 = 6

    ths = []
    for i in range(n):
        transit_time = random.random() * (t2 - t1) + t1
        arrive_time = random.random() * (t4 - t3) + t3
        ths.append(
            threading.Thread(
                target=poizd,
                args=(transit_time, arrive_time),
                name=f"Поїзд {i}"
            )
        )
        print(
            f"Поїзд {i} прибув {arrive_time:6.3f} "
            f"і проходить {transit_time:6.3f}"
        )

    for th in ths:
        th.start()
    for th in ths:
        th.join()
    log("всі поїзди пройшли")