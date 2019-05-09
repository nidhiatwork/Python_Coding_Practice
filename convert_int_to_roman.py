
"""
1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""
def convert_s(num):
        dic = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}

        res = ""
        
        keys = sorted(dic.keys(), reverse=True)
        
        while num != 0:
            
            for key in keys:
                if num/key >=1:
                    dividend = num // key
                    num = num % key
                    break
            
            res += dividend * dic[key]
        
        return res
        

print(convert_s(1994))