'''
Given an array of integers, find if the array contains any duplicates.
'''
def containsDuplicate(l):
    s=set()
    for item in l:
        if item in s:
            return False
        s.add(item)
    return True

l = [1,2,3,1]
print(containsDuplicate(l))