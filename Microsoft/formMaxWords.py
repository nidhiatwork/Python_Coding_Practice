
import collections
def solution(S, L):
    max_count = 0
    for word in L:
        current_count = 0
        s_counter = collections.Counter(S)
        l_counter = collections.Counter(word)
        timeToBreak = False
        while(not timeToBreak):
            for key in l_counter:
                if key not in s_counter or s_counter[key]-l_counter[key]<0:
                    timeToBreak = True
                    break
                else:
                    s_counter[key]-=l_counter[key]
            if not timeToBreak:
                current_count+=1
                max_count = max(max_count, current_count)
    return max_count

S = "BILL"
L = ["BILL", "BOB"]
print(solution(S, L))