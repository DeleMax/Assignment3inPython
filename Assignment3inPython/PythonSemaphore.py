from threading import Thread, Lock, RLock, Semaphore
import threading
import time
import random

class ActivePool(object):
    def __init__(self):
        super(ActivePool, self).__init__()
        self.active = []
        self.lock = threading.Lock()
    def randomNumber(self):
        return random.randint(0,1)
    def busyCode(self):
        time.sleep(1)
    def nonCriticalCode(self):
            time.sleep(1)
    def criticalCode(self):
            time.sleep(1)
    def write(self, semaphore):
        semaphore.acquire()
        time.sleep(1)
        semaphore.release()

def PrintSemaphore(self, activePool, semaphore):
      randomNumber = random.randint(0,1)
      with self:
          name = threading.currentThread().getName()
      if randomNumber == 0:
          for i in range(0, 2):
              print(name + " is now ready to write the shared resource.\n")
              activePool.nonCriticalCode()
              print(name + " has finished writing the shared resource.\n")
      else:
          for i in range(0, 2):
              print(name +  " is now ready to read the shared resource.\n")
              activePool.write(semaphore)
              print(name + " has finished reading the shared resource.\n")

semaphore = Semaphore(1)
activePool = ActivePool()
s = threading.Semaphore(1)
for i in range(7):
    t = threading.Thread(target=PrintSemaphore, args=(s, activePool, semaphore))
    t.start()
