def runLengthEncoding(string):
    ct=1
    ans=""
    for i in range(len(string)-1):
        if string[i]==string[i+1]:
            if ct==9:
                ans+=str(ct)+string[i]
                ct=0
            ct+=1
        else:
            ans+=str(ct)+string[i]
            ct=1
    ans+=str(ct)+string[-1]
    return ans
