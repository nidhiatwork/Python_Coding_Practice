'''
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]: direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.
'''

def stringShift_UsingAllShifts(s, shift):
    for shft in shift:
        direction, amount = shft[0], shft[1]
        if direction == 0:
            while amount:
                s = s[1:]+s[0]
                amount-=1
        else:
            while amount:
                s = s[-1]+s[:-1]
                amount-=1
    return s
    
def stringShift_UsingDiffShifts(s, shifts):
    count = 0
    for x,y in shifts:
        if x==0:
            count+=y
        else:
            count-=y
    count = count % len(s)
    return s[count:] + s[:count]

s = "abcdefg"
shifts = [[1,1],[1,1],[0,2],[1,2]]
print(stringShift_UsingDiffShifts(s, shifts))