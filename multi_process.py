from queue import Queue
from threading import Thread

def multiProcess(target, workers:Queue, thread:int=5):
    '''
        多线程实例代码
    '''
    threads = [
        Thread(target=target, args=(workers,)) for _ in range(thread)
    ]
    for t in threads:
    t.start()

    workers.join()

    while threads:
        threads.pop().join()
