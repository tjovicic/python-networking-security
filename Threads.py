#!/usr/bin/python3

import threading


class MyThread(threading.Thread):
    def __init__(self, num, val):
        threading.Thread.__init__(self)
        self.threadNum = num
        self.loopCount = val

    def run(self):
        print("Starting run: ", self.threadNum)
        myfunc(self.threadNum, self.loopCount)


def myfunc(num, val):
    count = 0
    while count < val:
        print(num, " : ", val * count)
        count = count + 1


def main():
    t1 = MyThread(1, 15)
    t2 = MyThread(2, 20)
    t3 = MyThread(3, 25)
    t4 = MyThread(4, 30)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    threads = [t1, t2, t3, t4]
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()
