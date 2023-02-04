def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""

def keypad(num):
    if num==0:
        return [""]
    keys_list = []
    for c in str(num):
        keys_list.append(get_characters(int(c)))
    
    combinations = [""]
    index = 0 
    return keypad_helper(keys_list, index, combinations)

def keypad_helper(keys_list, index, combinations):
    if index==len(keys_list):
        return combinations
    ans = []
    for comb in combinations:
        for c in keys_list[index]:
            ans.append(comb + c)
    combinations = list(ans)
    return keypad_helper(keys_list, index+1, combinations)

print(keypad(23))