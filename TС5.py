import random
import threading
import logging
from time import sleep, time

logging.basicConfig(level=logging.DEBUG)

N = 1
semaphore = threading.Semaphore(N)
lock = threading.Lock()
start = time()
q = 0 #кількість клієнтів, які розмовляють з оператором
result = 0 #кількість клієнтів, телефонуватимуть опепратору, коли лінія зайнята


def log(message):
    t = time() - start
    name = threading.current_thread().getName()
    logging.debug("[%6.3f] %s: %s", t, name, message)

def client(arr_time, call_time, next_time):
    global q, result
    sleep(arr_time)
    log("клієнт дзвонить до оператора")

    with lock:
        if q == N:
            result += 1
            log("кладе трубку і чекає, щоб зателефонувати оператору")
            sleep(next_time)



    with semaphore:

        with lock:
            q +=1
        log("триває розмова")
        sleep(call_time)

        with lock:
            q -= 1
        log("закінчили розмову")




if __name__=="__main__":
    n = 5
    T1 = 2
    T2 = 5
    T3 = 0
    T4 = 3
    T5 = 6
    T6 = 8
    threads = []
    for i in range(n):
        arrive_time = random.random() * (T2 - T1) + T1 #час надходження дзвінків
        call_time = random.random() * (T4 - T3) + T3 #час розмови
        next_time = random.random() * (T6 - T5) + T5 #час очікування
        thread = threading.Thread(
            name=f"Клієнт {i}",
            target = client,
            args=(arrive_time, call_time, next_time)
        )
        threads.append(thread)
        print(
            f"Клієнт {i} додзвонився до оператора о {arrive_time:6.3f}"
            f"розмова триває {call_time:6.3f}"
            f"кладе трубку і чекає щоб зателефонувати вільному операторатору {next_time:6.3f}"
        )
    for i in range(n):
        threads[i].start()
    for i in range(n):
        threads[i].join()
    log("всі клієнти зідзвонились з операторами")
