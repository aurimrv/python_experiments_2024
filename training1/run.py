from training1 import Training

def main():
   print("Type an integer number: ", end="")
   n = int(input())

   fact = Training.factorial(n)

   if (fact is None):
      print("Error: there is no factorial for negative numbers")
   else:
      print("Factorial of %d is %d." % (n, fact))

if (__name__ == '__main__'):
   main()