'''
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
Input: "abbaca"
Output: "ca"
'''

def removeDuplicates(S):
    st=[]
    for c in S:
        if st and c==st[-1]:
            st.pop()
        else: 
            st.append(c)
    return "".join(st)

S = "abbaca"
print(removeDuplicates(S))
