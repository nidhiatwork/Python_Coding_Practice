# Determine whether or not a given string contains no duplicate characters.

def contains_no_duplicates(string):
  letters = set()
  for letter in string:
    if letter in letters:
      return False
    letters.add(letter)
  return True

if __name__ == "__main__":
  import sys
  print(contains_no_duplicates("Nidhi"))