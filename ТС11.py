from threading import Timer
from queue import Queue
from time import time, sleep
import random
import logging


logging.basicConfig(level=logging.DEBUG)


w = Queue(maxsize=1)
start = time()


def poizd(transit_time, index):
    logging.debug("Поїзд {} прибув до ділянки".format(index))
    w.put(index)
    logging.debug("Поїзд {} почав проходити ділянку".format(index))
    sleep(transit_time)
    index = w.get()
    logging.debug("Поїзд {} пройшов ділянку".format(index))
    print("Поїзд {} пройшов ділянку. Повний час подорожі {:.4f}"
          .format(index, time() - start))


def next_poizd(t1, t2, t3, t4, index):
    transit_time = random.random() * (t2 - t1) + t1
    arrive_time = random.random() * (t4 - t3) + t3
    print("Поїзд {} прибуває через {:.4f} секунд і проходить "
          "ділянку за {:.4f} секунд"
          .format(index, arrive_time, transit_time))
    th = Timer(arrive_time, poizd, args=(transit_time, index))
    th.start()
    return th


if __name__ == 'main':
    n = 21
    t1 = 3
    t2 = 1
    t3 = 0
    t4 = 6

    ths = []
    for i in range(n):
        ths.append(next_poizd(t1, t2, t3, t4, i))
    for i in range(n):
        ths[i].join()