def fibonacci_sequencer():
  while True:
    length=int(input("Please enter the desired length of Fibonacci sequence."))
    if length>0:
      print("Generating Fibonacci sequence now...")
      fib_array=[0,1]
      count=0
      for n in range(0, length-2):
        count+=1
        fib_array.append(fib_array[count]+fib_array[count-1])
      print (fib_array)
      break

#Calling the fibonacci_sequencer function
fibonacci_sequencer()
