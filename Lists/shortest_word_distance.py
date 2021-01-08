'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3'''


def shortestDistance(words, word1, word2):
    ans = float('inf')
    x1 = x2 = -1
    for i,word in enumerate(words):
        if word==word1: 
            x1 = i
        if word==word2:
            x2 = i
        if x1!=-1 and x2!=-1:
            ans = min(ans, abs(x1-x2))
    return ans

print(shortestDistance(["practice", "makes", "perfect", "coding", "makes"],"coding", "practice"))