

def stringCompare(s1,s2):
    st1 = createStack(s1)
    st2 = createStack(s2)
    return st1 == st2

def createStack(s):
    st = []
    for c in s:
        if c=='#':
            if st:
                st.pop()
        else: 
            st.append(c)
    return st
    

s1 = 'ac#b'
s2 = 'ad#b'
print(stringCompare(s1, s2))