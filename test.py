def Hello():
   print("Hello, World!")

def IsPrimo(int n):
   for i in range(2, int(n**0.5) + 1):
       if n % i == 0:
           return False
   return True

def primos(int a, int b):
   return [n for n in range(a, b + 1) if IsPrimo(n)]
   