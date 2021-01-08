def smallestSetCoveringIntervals(first, last):
    first.sort()
    last.sort()
    for i in range(len(first)):
        interval = []
        for j in range(first[i],last[i]+1):
            interval.append(j)
        if len(interval)<4 or len(interval)%2:
            return 0
        ct1,ct2=0,0
        for item in interval:
            if item in first:
                ct1+=1
            if item in last:
                ct2+=1
        if ct1>=2 and ct2>=2:
            return True
    return False
first= [3, 2, 0, 4]
last= [6, 4, 2, 7]
print(smallestSetCoveringIntervals(first, last))