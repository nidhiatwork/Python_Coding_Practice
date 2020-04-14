
T = int(input())
t=1
while t<=T:
    N = int(input())
    strs = []
    ans = ""
    for i in range(N):
        inp = input()
        strs.append(inp)
    
    base = strs[0]
    b_pre, b_post = base.split("*")
    for i in range(1, len(strs)):
        pref,postf = strs[i].split("*")
        if pref and b_pre:
            if b_pre.find(pref)!=0 and pref.find(b_pre)!=0:
                ans = "*"
                break
        if len(pref)>len(b_pre):
            b_pre = pref
        if postf and b_post:
            if b_post.find(postf)!=len(b_post)-len(postf) and postf.find(b_post)!=len(postf)-len(b_post):
                ans = "*"
                break
        if len(postf)>len(b_post):
            b_post = postf
        ans = b_pre + b_post
    print(f'Case #{t}: {ans}')
    t+=1