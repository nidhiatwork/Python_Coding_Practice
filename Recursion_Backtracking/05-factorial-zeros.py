# Count the number of zeros at the end of a factorial.

def factorial_zeros(n):
  five_factors = 0
  while n > 4:
    n //= 5
    five_factors += n
  return five_factors

import unittest

print(factorial_zeros(7))

