
T = int(input())
t=1
while t<=T:
    s = input().strip()
    open_brackets = 0
    result = ""
    for c in s:
        val = int(c)
        if val>open_brackets:
            result +=(val-open_brackets)*'('+c
        elif val<open_brackets:
            result +=(open_brackets-val)*')'+c
        else:
            result +=c
        open_brackets=val
    if open_brackets:
        result +=open_brackets*')'
    ans = "Case #"+str(t)+": "+result
    print(ans)
    t+=1
