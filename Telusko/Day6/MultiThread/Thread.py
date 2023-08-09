from threading import *
from time import sleep

class Hello(Thread):

    def run(self):
        for i in range(500):
         print("Hello")
         sleep(1)




class Hi(Thread):

    def run(self):
        for i in range(0,500):
          print("Hi")
          sleep(1)


hello = Hello()
hi = Hi()

hello.start()
hi.start()
