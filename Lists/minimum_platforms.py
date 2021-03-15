'''Given arrival and departure times of all trains that reach a railway station, the task is to find the minimum number of platforms required for the railway station so that no train waits.
We are given two arrays that represent arrival and departure times of trains that stop.

Examples:
Input: arr[] = {9:00, 9:40, 9:50, 11:00, 15:00, 18:00}
dep[] = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
Output: 3
'''
def minimumPlatform(n,arr,dep):
    # code here
    arr.sort()
    dep.sort()
    i=1
    j=0
    platforms = 1
    result = 1
    while i<n and j<n:
        if arr[i]<=dep[j]:
            platforms+=1
            i+=1
        else:
            platforms-=1
            j+=1
        result = max(result,platforms)
    return result

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print(minimumPlatform(len(arr),arr,dep))