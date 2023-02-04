def caesarCipherEncryptor(string, key):
    ans=""
    for c in string:
        new_ascii = ord(c)+key
        if new_ascii>122:
            times=new_ascii//122
            new_ascii=((new_ascii-122*times)%26)+96
        ans+=chr(new_ascii)
    return ans
string="abc"
key=57
print(caesarCipherEncryptor(string, key))