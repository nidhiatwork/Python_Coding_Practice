'''You have n  letters. Return the number of possible non-empty sequences of letters you can make using the letters.
Input: letters = "AAB"
Output: 8
"A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"
'''

class Solution:

    def helper(self, letters, path, visited):
        if path and path not in visited:
            visited.add(path)
        for i in range(len(letters)):
            self.helper(letters[:i]+letters[i+1:], path+letters[i], visited)
   
    def numOfPossibilities(self, letters: str) -> int:
        visited = set()
        self.helper( letters, "", visited)
        return len(visited)

letters = "ABC"
s=Solution()
print(s.numOfPossibilities(letters))