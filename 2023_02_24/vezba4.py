import concurrent.futures.thread as t
import time

executor = t.ThreadPoolExecutor(10)

def f():
    print("Hello world")
    time.sleep(1)
    print("How are you")

for i in range(1000):
    executor.submit(f)