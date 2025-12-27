import time
def mytime():
   t1=time.perf_counter()
   num=int(input("Enter a number: "))
   if num>0:
      print(f"the number {num} is positive")
   else:
      print(f"the number {num} is negative or zero")
   t2=time.perf_counter()
   print(f"time taken to execute the code is {t2-t1} seconds")



mytime()
mytime()
mytime()
#Time taken to execute the program








