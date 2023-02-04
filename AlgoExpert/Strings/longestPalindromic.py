def longestPalindromicSubstring(string):
    map=dict()
    longest_pal=[]
    solveForLongestPal(string, map, longest_pal, i=0, j=len(string)-1)
    print(longest_pal)

def solveForLongestPal(string, map, longest_pal, i, j):
    if i>j or (i,j) in map:
        return
    map[(i,j)]=1
    if isPalindrome(string,i,j):
        if not longest_pal:
            longest_pal.append(string[i:j+1])
        elif j-i+1>len(longest_pal[0]):
            longest_pal.pop()
            longest_pal.append(string[i:j+1])
            
    solveForLongestPal(string, map, longest_pal,i+1,j)
    solveForLongestPal(string, map, longest_pal,i,j-1)
    

def isPalindrome(string, i, j):
    rev = string[i:j+1][::-1]
    return string[i:j+1]==rev

string = "abaxyzzyxf"
print(longestPalindromicSubstring(string))