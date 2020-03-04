'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess( num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
'''


def guessNumber(n) :
    low = 1
    hi = n
    while (low <=hi):
        print("low ",low," hi ",hi)
        mid = (hi+low)//2
        if (guess(mid) == 0):
            return mid
        elif (guess(mid) < 0):
            hi = mid - 1
        else:
            low = mid + 1
    return -1


def guess(n):
    if n<6:
        return 1
    elif n>6:
        return -1
    return 0


n = 10
pick = 6
print(guessNumber(n))

