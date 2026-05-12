# Write a Python program that creates a worker thread which prints “Hello
# from worker thread” while the main thread prints “Hello from main thread”, and
# ensure that the main thread waits for the worker thread to finish execution
# before the program exits

import  threading
def worker():
    print("Hello from worker main thread")

t1 = threading.Thread(target=worker)
t1.start()
 t1.join()
print("Hello from main thread")

# Write a Python program that creates three separate threads where each
# thread prints numbers from 1 to 5, and every printed number must be prefixed
# with the name of the thread that printed it, such as “Thread-1: 3

import threading

def task(n):
    for i in range(1,n):
        print(f"{threading.current_thread().name}:{i}")
t1 = threading.Thread(target=task,name="Thread-1",args=(6,))
t2 = threading.Thread(target=task,name="Thread-2",args=(6,))
t3 = threading.Thread(target=task,name="Thread-3",args=(6,))

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

# Write a Python program in which a thread accepts two integer arguments,
# computes their sum, prints the result from inside the thread, and ensures that
# the main thread waits until the worker thread completes execution.

import threading

def task(a,b):
    result= a+b
    print("Sum from worker thread:",result)
t = threading.Thread(target=task,args=(5,7))
t.start()
t.join()
print("Main thread finished")

# Write a Python program where two threads increment a shared variable named
# counter exactly 100000 times each without using any synchronization mechanism,
# and print the final value of the counter to demonstrate inconsistent or
# incorrect results caused by a race condition.


import threading
counter=0
def task():
    global counter
    for i in range(100000):
        counter +=1
t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)
t1.start()
t2.start()
t1.join()
t2.join()
print("Final counter value:",counter)

# Modify the previous program so that the shared variable counter is updated
# in a thread-safe manner using threading.Lock, and ensure that the final printed
# value of the counter is always correct

import threading
counter = 0
lock = threading.Lock()
def task():
    global counter
    for i in range(100000):
        with lock:
            counter +=1
t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)
t1.start()
t2.start()
t1.join()
t2.join()
print("Final counter value:", counter)

# Write a Python program where one thread prints “A started” and then sleeps
# for two seconds, another thread prints “B started”, and the execution order is
# controlled in such a way that the second thread starts only after the first
# thread has completely finished

import threading
import time
def task1():
    print('A Started')
    time.sleep(2)
    print('A Finished')
def task2():
    print('B Started')

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t1.start()
t1.join()
t2.start()
t2.join()

# Write a Python program in which three worker threads wait until a
# synchronization signal is received, the main thread sleeps for two seconds and
# then signals all waiting threads using an event, after which each worker thread
# prints a message indicating that it has started execution

import threading
import time
a = threading.Event()
def task(name):
    print(f"{name} is waiting for a signal...")
    a.wait()
    print(f"{name} has starting execution")

t1 = threading.Thread(target=task, args=("Thread-1",))
t2 = threading.Thread(target=task, args=("Thread-2",))
t3 = threading.Thread(target=task, args=("Thread-3",))


t1.start()
t2.start()
t3.start()

time.sleep(2)

print("Main thread sends the signal")

a.set()
t1.join()
t2.join()
t3.join()
print("All threads completed")


# Write a Python program that creates five threads competing for a shared
# resource, restricts access so that only two threads can enter the critical
# section at the same time using a semaphore, and prints a message whenever a
# thread enters and exits the critical section.

import threading
s=threading.Semaphore(3)
x=0
def fun1():
    global x
    with s:
        x+=1
        print(x)
        print(f"{threading.current_thread().name} thread done")

t1=threading.Thread(target=fun1,name="Thread-1")
t2=threading.Thread(target=fun1,name="Thread-2")
t3=threading.Thread(target=fun1,name="Thread-3")
t4=threading.Thread(target=fun1,name="Thread-4")
t5=threading.Thread(target=fun1,name="Thread-5")
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
print("main thread done")


# Write a Python program that starts a daemon thread running an infinite
# loop which repeatedly prints “Running in background”, while the main thread
# sleeps for two seconds and then exits, and observe what happens to the daemon
# thread when the main program terminates.

import threading
def fun():
    while True:
        print("infinte loop running")
t1=threading.Thread(target=fun,name="Thread-1",daemon=True)
t2=threading.Thread(target=fun,name="Thread-2",daemon=True)
t1.start()
t2.start()
print("main thread done")


# Write a Python program using ThreadPoolExecutor with three worker threads
# that submits tasks to compute the square of numbers from 1 to 5 and prints each
# result as soon as the corresponding task completes

from concurrent.futures import ThreadPoolExecutor
def fun(x):
    print("inside fun")
    return x+1
l=[1,2,3,4,5]
with ThreadPoolExecutor(max_workers=3) as executor:
    futures= [executor.submit(fun, i) for i in l]
    futures2=executor.map(fun,l)
    for i in futures2:
        print(i)