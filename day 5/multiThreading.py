# Multi-Threading is process of executing multiple threads concurrently. It allows you to run multiple tasks at the same time, which can improve the performance of your program.
# A thread is a lightweight process that can run concurrently with other threads. It shares the same memory space and resources of the parent process, which allows for efficient communication and data sharing between threads.


# from time import sleep
# from threading import threading 

# def first():
#     for i in range(2):
#         print("Aarush")
# def second():
#     for i in range(2):
#         print("Parate")
# first()
# second()

from time import sleep
from threading import Thread

class A(Thread):
    def run(self):
        for i in range(2):
            print("Aarush")
            sleep(1)
class B(Thread):
    def run(self):
        for i in range(2):
            print("Parate")
            sleep(1)

a = A()
b = B() 
a.start()
b.start()   
