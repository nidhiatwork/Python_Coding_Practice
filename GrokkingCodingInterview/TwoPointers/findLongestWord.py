'''Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
'''

def findLongestWord(s, d):
    ans = ""
    for item in d:
        i,j=0,0
        while i<len(s) and j<len(item):
            if s[i]==item[j]:
                i+=1
                j+=1
            else:
                i+=1
        if j==len(item):
             if len(item)>len(ans) or (len(item)==len(ans) and item<ans):
                 ans = item
    return ans

s = "abpcplea"
d = ["ale","apple","monkey","plea"]
s = "bab"
d = ["ba","ab","a","b"]
print(findLongestWord(s, d))