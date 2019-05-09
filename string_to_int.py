

import math
def convert_s(str):
        str=str.strip()
        if not str:
                return 0
        val=""
        if not str[0].isdigit() and str[0] not in ["-","+"]:
                return 0
        if str[0] in ["-","+"]:
                val+=str[0]
                str=str[1:]
        for i in range(len(str)):
                if not str[i].isdigit():
                        break
                val+=str[i]
        if val=="+" or val=="-":
                return 0
        elif int(val)>math.pow(2,31)-1:
                val = math.pow(2,31)-1
        elif int(val)<math.pow(-2,31):
                val = math.pow(-2,31)
        return int(val)

print(convert_s("-91283472332"))