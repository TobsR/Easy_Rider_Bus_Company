import math


x = int(input())
logistic_func = pow(math.e, x) / (pow(math.e, x) + 1)
print(round(logistic_func, 2))
