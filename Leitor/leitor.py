import threading
import time


class SharedResource:
    def __init__(self):
        self.value = 0


class RWControll:
    def __init__(self):
        self.readers = 0
        self.mutex = threading.Semaphore(1)
        self.lock = threading.Semaphore(1)

    def read_acquire(self):
        self.mutex.acquire()
        self.readers += 1
        if self.readers == 1:
            self.lock.acquire()
        self.mutex.release()

    def read_release(self):
        self.mutex.acquire()
        self.readers -= 1
        if self.readers == 0:
            self.lock.release()
        self.mutex.release()

    def write_acquire(self):
        self.lock.acquire()

    def write_release(self):
        self.lock.release()


def read(lock, res):
    lock.read_acquire()
    print(threading.current_thread().ident, "Reading:", res.value)
    time.sleep(1.5)
    lock.read_release()


def write(lock, res):
    lock.write_acquire()
    print(threading.current_thread().ident, "Writing")
    res.value += 1
    time.sleep(1)
    lock.write_release()


def executeDemo():
    lock = RWControll()
    res = SharedResource()

    writer1 = threading.Thread(
        target=write,
        args=(
            lock,
            res,
        ),
    )
    writer2 = threading.Thread(
        target=write,
        args=(
            lock,
            res,
        ),
    )
    writer3 = threading.Thread(
        target=write,
        args=(
            lock,
            res,
        ),
    )

    reader1 = threading.Thread(
        target=read,
        args=(
            lock,
            res,
        ),
    )
    reader2 = threading.Thread(
        target=read,
        args=(
            lock,
            res,
        ),
    )
    reader3 = threading.Thread(
        target=read,
        args=(
            lock,
            res,
        ),
    )
    reader4 = threading.Thread(
        target=read,
        args=(
            lock,
            res,
        ),
    )

    writer1.start()
    reader1.start()
    writer2.start()
    writer3.start()
    reader2.start()
    reader3.start()
    reader4.start()
