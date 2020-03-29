
def getStrength(password,weight_a):
    strength=[]
    for c in password:
        x=(ord(c)-97)+weight_a
        if x>=26:
            x=x-26
        strength.append(x)
    print(strength)
    return sum(strength)

password,weight_a = "fiy",2
print(getStrength(password,weight_a))