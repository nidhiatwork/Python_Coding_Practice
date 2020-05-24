'''
You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
'''

def checkRecord_1(s):
    firstA = False
    for i,c in enumerate(s):
        if c=='A':
            if not firstA:
                firstA = True
            else:
                return False
        if s[i:i+3]=='LLL':
            return False
    return True

def checkRecord_2(s):
    return s.count('A')<2 and s.count('LLL')==0

s = "PPALLL"
print(checkRecord_1(s))
