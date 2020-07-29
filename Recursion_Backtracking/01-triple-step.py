# Give the number of ways to climb n steps 1, 2, or 3 steps at a time.

s = dict()

def triple_step(n):
  if n<0:
        return 0
  if n==0:
        return 1
  if n in s:
        return s[n]
  s[n] =  triple_step(n-1) + triple_step(n-2) + triple_step(n-3)
  return s[n]

import unittest

class Test(unittest.TestCase):
  def test_triple_step(self):
    self.assertEqual(triple_step(3), 4)
    self.assertEqual(triple_step(7), 44)

if __name__ == "__main__":
  unittest.main()

