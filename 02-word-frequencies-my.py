"""
Report word frequencies for a text.
"""
from collections import Counter
import unittest
class TextHandler:
      def __init__(self, lines):
            self.word_count = Counter()
            self.total_words = 0
            lines = lines.strip().split("\n")
            for line in lines:
                  words = line.strip().split(" ")
                  for word in words:
                    self.word_count[word]+=1
                    self.total_words+=1
      
      def word_frequency(self, word):
            return self.word_count[word]/self.total_words
  

text = """
        When the sun shines, we'll shine together
        Told you I'd be here forever
        Said I'll always be a friend
        Took an oath I'ma stick it out 'til the end
        Now that it's raining more than ever
        Know that we'll still have each other
        You can stand under my umbrella
        You can stand under my umbrella
        (Ella ella eh eh eh)
        Under my umbrella
        (Ella ella eh eh eh)
        Under my umbrella
        (Ella ella eh eh eh)
        Under my umbrella
        (Ella ella eh eh eh eh eh eh)"""


class TestTextHandler(unittest.TestCase):
      def test_textHandler(self):
            handler = TextHandler(text)
            print(handler.word_count)
            self.assertEqual(handler.total_words,87)
            self.assertEqual(handler.word_frequency("umbrella"),5/87)

if __name__=="__main__":
  unittest.main()