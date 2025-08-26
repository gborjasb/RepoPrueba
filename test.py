def Hello():
   print("Hello, World!")

def IsPrimo(int n):
   for i in range(2, int(n**0.5) + 1):
       if n % i == 0:
           return False
   return True

def primos(int a, int b):
   return [n for n in range(a, b + 1) if IsPrimo(n)]


# Cambios

# Mas Cambios

def RungeKuttaMethod(f, y0, t0, t1, h):
    n = int((t1 - t0) / h)
    t = t0
    y = y0
    for i in range(n):
        k1 = h * f(t, y)
        k2 = h * f(t + h / 2, y + k1 / 2)
        k3 = h * f(t + h / 2, y + k2 / 2)
        k4 = h * f(t + h, y + k3)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += h
    return y