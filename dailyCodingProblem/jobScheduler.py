import time


def scheduler(f,n):
    time.sleep(n/1000)
    return f()

def log():
    print("Function has been executed")

scheduler(log, 4000);