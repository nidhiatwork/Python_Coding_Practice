'''
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included.

Given a number n, the task is to find n’th Ugly number.
Input  : n = 7
Output : 8

Input  : n = 10
Output : 12

Input  : n = 15
Output : 24

Input  : n = 150
Output : 5832
'''

def findUglyNum(n):
    ugly = [None]*n
    ugly[0]=1

    i2,i3,i5=0,0,0

    next_multiple_of_2 = ugly[i2]*2;
    next_multiple_of_3 = ugly[i3]*3
    next_multiple_of_5 = ugly[i5]*5;


    for i in range(1,n):
        ugly_num = min(next_multiple_of_2,next_multiple_of_3,next_multiple_of_5)
        ugly[i]=ugly_num
        if(next_multiple_of_2 == ugly_num):
            i2+=1
            next_multiple_of_2=ugly[i2]*2
        if(next_multiple_of_3 == ugly_num):
            i3+=1
            next_multiple_of_3=ugly[i3]*3
        if(next_multiple_of_5 == ugly_num):
            i5+=1
            next_multiple_of_5=ugly[i5]*5
    return ugly_num

print(findUglyNum(42))