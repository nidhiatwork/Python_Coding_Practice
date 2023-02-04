from collections import Counter
def wordScramble(words, s):
    s_counter = Counter(s)
    for word in words:
        isMatch = True
        word_counter = Counter(word)
        for k,v in word_counter.items():
            if k not in s_counter or v>s_counter[k]:
                isMatch = False
                break
        if isMatch:
            return word
    return "-"

words = ["baby", "referee", "cat", "dada", "dog", "bird", "ax"]
string1 = "ctay"
string2 = "bcanihjsrrrferet"
string3 = "tbaykkjlga"
string4 = "bbbblkkjbaby"
string5 = "dad"
string6 = "breadmaking"
print(wordScramble(words, string6))