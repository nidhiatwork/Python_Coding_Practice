'''Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

'''

from collections import Counter

def next_num(num):
    result = 0
    while num:
        result = result + (num%10)**2
        num=num//10
    return result

def find_happy_num(num):
    slow,fast = num,num
    while True:
        slow = next_num(slow)
        fast = next_num(next_num(fast))
        if slow==fast:
            break
    return slow==1


num = 23
print(find_happy_num(num))