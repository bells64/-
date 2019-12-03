import math
# -
m = 2 # благо получные исходы(int)
n = 16 # общее кол-во исходов(int)
c = math.factorial(n) / math.factorial(n - m) - math.factorial(m)
print(c)