'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''

def twoSum(numbers,target):
    i,j=0,len(numbers)-1
    while i < j:
        if numbers[i]+numbers[j]<target:
            i+=1
        elif numbers[i]+numbers[j]>target:
            j-=1
        else:
            return[i+1,j+1]

def twoSum_2(numbers, target):
    dic = {}
    for i, num in enumerate(numbers):
        if target-num in dic:
            return [dic[target-num]+1, i+1]
        dic[num] = i

def twoSum_3(numbers, target):
    investigatedSoFar = []
    for i in range(len(numbers)):
        if not numbers[i] in investigatedSoFar:
            investigatedSoFar.append(numbers[i])
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l) // 2
                if numbers[mid] == tmp:
                    return([i + 1, mid + 1])
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1

numbers,target = [2,7,11,14,8,6,15],14
print(twoSum_3(numbers,target))
