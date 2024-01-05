
#! they aren't important for the program to run
#! program doesn't wait daemon threads finishes
#! bg tasks, garbage collect, input, long processes

import threading, time

def timer():
      print()
      count = 0
      while True: #! ETERNAL LOOP NEVER FINISHES
            time.sleep(1)
            count+=1
            print("Logged in for : ", count, "seconds")
            
# x = threading.Thread(target=timer) #! NEVER FINISHES
# x.start()

x = threading.Thread(target=timer, daemon=True) 
x.setDaemon(True) #! DEPRECATED USE ABOVE
x.start()

print(x.isDaemon)

answer = input("Do you wish to exit?")





