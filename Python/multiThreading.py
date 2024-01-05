import threading, time

def eat():
      time.sleep(3)
      print("You ate food!")
      
def drink():
      time.sleep(2)
      print("You drank beverage!")
      
def work():
      time.sleep(1)
      print("You finished tasks!")
      
# eat()       #! SEQUENTIALLY
# drink()    #! NOT CONCURRENTLY
# work()    #! ONE BY ONE

x = threading.Thread(target=eat, args=())
x.start()

y = threading.Thread(target=drink, args=())
y.start()

z = threading.Thread(target=work, args=())
z.start()

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

