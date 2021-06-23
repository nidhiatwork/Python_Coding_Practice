'''
"340012"
Three lac fourty thousand and twelve
'''

ones = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten","eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
ties = {2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}
bigs = {3:"hundred", 4:"thousand", 5:"thousand", 6:"lac", 7:"lac", 8:"crore", 9:"crore"}

def convert(money):
    l = len(money)
    if l==0:
        return ""
    if money[0]=='0':
        return convert(money[1:])
    if l==1:
        return ones[int(money[-1])]
    if l==2:
        if int(money)<20:
            return teens[int(money[-1])%10]
        else:
            return ties[int(money[0])] + " " + convert(money[1:])
    if l==3 or not l%2:
        return ones[int(money[0])] + " " + bigs[l] + " " + convert(money[1:])
    
    if l%2:
        return convert(money[:2]) + " " + bigs[l] + " " + convert(money[2:])

if __name__=='__main__':
    num = "3870000"
    print(convert(num))