'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
'''
import itertools
def backspaceCompare_1(S,T):
    def F(S):
        skip = 0
        for x in reversed(S):
            if x == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                print("yield x: "+x)
                yield x

    return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))

def backspaceCompare_2(S, T):
        s=list()
        t=list()
        for c in S:
            if c!='#':
                s.append(c)
            else:
                if len(s)==0:
                    continue
                s.pop()
        for c in T:
            if c!='#':
                t.append(c)
            else:
                if len(t)==0:
                    continue
                t.pop()
        return ''.join(s) == ''.join(t)

print(backspaceCompare_2('ab#c','ad#c'))