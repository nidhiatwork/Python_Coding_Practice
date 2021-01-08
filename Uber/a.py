'''
You are standing at the first element of a given array of integers. Your task is to move to the end of the array, collecting as many points as possible along the way. At each step you can move no more than k elements to the right. Each time you land on an element, its value is added to your score. What is the maximum score you can achieve at the end of the array?

Note: You must step on the final element of the array to end the journey.
'''

def arrayJourney(path, k):
    n = len(path)
    score = path[0]
    i = 0
    while i<len(path)-1:
        if i+k==n-1:
            mx_score = score+ path[n-1]
            for j in range(n-1,i,-1):
                score = score + path[j]
                if score>mx_score:
                    mx_score = score
            return mx_score
        mx = i+1
        for j in range(i+1,min(i+k+1,len(path))):
            if path[j]>path[mx]:
                mx = j
        i = mx
        score+=path[i]
    return score

path,k = [-3, 5, 13, 0, -17, 3, -19, -17, -13, 8],4
print(arrayJourney(path,k))