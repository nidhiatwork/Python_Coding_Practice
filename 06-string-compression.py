"""Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""
def compress(string):
  if len(string) == 0:
    return string
  parts = []
  current_letter = string[0]
  current_count = 1
  for letter in string[1:]:
    if current_letter == letter:
      current_count += 1
    else:
      parts.append(current_letter + str(current_count))
      current_letter = letter
      current_count = 1
  parts.append(current_letter + str(current_count))
  compressed = "".join(parts)
  if len(compressed) < len(string):
    return compressed
  else:
    return string

if __name__ == "__main__":
  import sys
  print(compress("Nibbbbbdhibbbbbbbb"))
