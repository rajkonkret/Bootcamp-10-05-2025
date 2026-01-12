import random
import time
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor

import numpy as np

total_points_inside_circle = 0


# def monte_carlo_pi(n):
#     points_inside_circle = 0
#
#     for _ in range(n):
#         x = random.uniform(-1, 1)
#         y = random.uniform(-1, 1)
#
#         if x ** 2 + y ** 2 <= 1:
#             points_inside_circle += 1
#
#     return 4 * (points_inside_circle / n)
#

#  z wykorzystaniem numpy
def monte_carlo_pi(num_sample):
    x = np.random.uniform(-1, 1, num_sample).astype(np.float32)
    y = np.random.uniform(-1, 1, num_sample).astype(np.float32)

    inside_circle = x ** 2 + y ** 2 <= 1
    num_inside_circle = np.sum(inside_circle)
    pi_estimate = 4 * num_inside_circle / num_sample

    return pi_estimate


def no_threads(iterations):
    start = time.time()
    pi = monte_carlo_pi(iterations)
    end = time.time()
    print(f"Bez wątków: {pi}, czas: {end - start}")


def with_threads(iterations):
    num_thread = 8
    iterations_per_thread = iterations // num_thread
    threads = []

    def thread_monte_carlo_pi():
        global total_points_inside_circle
        points_inside_circle_th = monte_carlo_pi(iterations_per_thread)
        with lock:
            total_points_inside_circle += points_inside_circle_th

    lock = threading.Lock()
    start = time.time()
    for _ in range(num_thread):
        thread = threading.Thread(target=thread_monte_carlo_pi)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    pi = total_points_inside_circle / num_thread
    end = time.time()
    print(f"Z wątkami: {pi}, czas {end - start}")


def with_processes(iterations):
    num_processes = 8
    iterations_per_process = iterations // num_processes

    start = time.time()
    with multiprocessing.Pool(num_processes) as pool:
        result = pool.map(monte_carlo_pi, [iterations_per_process] * num_processes)
        pi = sum(result) / num_processes
        end = time.time()

        print(f"Z procesami: {pi}, czas {end - start}")


def with_thread_pool_executor(iterations):
    num_threads = 8
    iterations_per_thread = iterations // num_threads

    start = time.time()
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        result = list(executor.map(monte_carlo_pi, [iterations_per_thread] * num_threads))
        pi = sum(result) / num_threads

    end = time.time()
    print(f"Z ThreadPoolExecutor: {pi}, czas {end - start}")


iterations = 10_000_000
if __name__ == '__main__':
    no_threads(iterations)
    with_threads(iterations)
    with_processes(iterations)
    with_thread_pool_executor(iterations)

# bez numpy
# Bez wątków: 3.1419448, czas: 3.4347798824310303
# Z wątkami: 3.1415864, czas 3.2730109691619873
# Z procesami: 3.1418223999999997, czas 0.8339979648590088
# Z ThreadPoolExecutor: 3.1413352, czas 3.2519681453704834

# z numpy
# Bez wątków: 3.1411896, czas: 0.38230204582214355
# Z wątkami: 3.1415856000000004, czas 0.10786271095275879
# Z procesami: 3.1410412, czas 0.29815006256103516
# Z ThreadPoolExecutor: 3.142298, czas 0.09321308135986328

