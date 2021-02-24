'''
Given an array of integers and a sum, the task is to print all subsets of given array with sum equal to given sum.

Examples:

Input : arr[] = {2, 3, 5, 6, 8, 10}
        sum = 10
Output : 5 2 3
         2 8
         10
'''

def printSubsets(arr,n,path,sum):
    if sum==0:
        print(path)
        return
    if n==0:
        return
    print("Follow without picking:",arr[n-1])
    printSubsets(arr,n-1,path,sum)
    new_path = [] + path
    new_path.append(arr[n-1])
    print("Follow by picking:",arr[n-1])
    printSubsets(arr,n-1,new_path,sum-arr[n-1])

arr = [ 2, 5, 8, 4, 6, 11 ] 
total = 13
path = []
printSubsets(arr,len(arr),path,total)