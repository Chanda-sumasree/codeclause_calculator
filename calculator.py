import math
from fractions import Fraction

# addition
num1 = int(input())
num2 = int(input())
result = num1 + num2
print(result) 

# subtraction
num1 = int(input())
num2 = int(input())
result = num1 - num2
print(result) 

# multiplication
num1 = int(input())
num2 = int(input())
result = num1 * num2
print(result) 

# division
num1 = int(input())
num2 = int(input())
result = num1 / num2
print(result) 

# logarithms
num = int(input())
base = int(input())
result = math.log(num, base)
print(result) 

# fractions
frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)
result = frac1 + frac2
print(result) 