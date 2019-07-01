"""
Count the number of zeros at the end of a factorial.
"""

"""
def factorial_zeros(n):
      five_factors = 0
  while n > 4:
    n //= 5
    five_factors += n
  return five_factors
  """
  
def find_factorial(num):
  if num==1:
        return 1
  factorial = num * find_factorial(num-1)
  return factorial

fact = find_factorial(55)
zeros = 0
multiply=10
while(fact>=1):
  if fact%multiply==0:
    zeros+=1
    multiply*=10
  else:
    break
print(zeros)