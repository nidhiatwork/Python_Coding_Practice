# Determine whether or not one string is a permutation of another.
import collections
def is_permutation(str1, str2):
  counter = collections.Counter()
  for letter in str1:
    counter[letter] += 1
  for letter in str2:
    if not letter in counter:
      return False
    counter[letter] -= 1
    if counter[letter] == 0:
      del counter[letter]
  return len(counter) == 0

def isPermutation_2(str1,str2):
    if len(str1)!=len(str2):
        return False
    c = collections.defaultdict(int)
    for i in range(len(str1)):
        c[str1[i]]+=1
        c[str2[i]]-=1
    for v in c.values():
        if v!=0:
            return False
    return True

if __name__ == "__main__":
  import sys
  print(is_permutation("nidhi", "indhi"))
