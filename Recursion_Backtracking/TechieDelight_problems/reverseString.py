def reverseString(s,l,h):
    if l>=h:
        return ''.join(s)
    s[l],s[h]=s[h],s[l]
    return reverseString(s,l+1,h-1)

s='Nidhi'
print(reverseString(list(s),0,len(s)-1))