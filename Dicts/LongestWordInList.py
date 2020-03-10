'''
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
'''
def longestWord(words):
    words.sort(key = lambda x: (-len(x),x))
    print(words)
    for word in words:
            if all(word[:k] in words for k in range(1, len(word))):
                return word
    return ""

    
    
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
print(longestWord(words))