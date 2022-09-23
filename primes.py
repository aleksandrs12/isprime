import math

for j in range(1, 100):
    if (math.factorial(j-1) + 1) % j == 0:
        print(j)