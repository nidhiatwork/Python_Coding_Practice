"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""
phone = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}
output = []

def letterCombinations(digits):                   
    if digits:
        backtrack("", digits)
    return output


def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                print("Combination done: ", combination)
                output.append(combination)
            else:
                for letter in phone[next_digits[0]]:
                    print("letter: ",letter)
                    print("Triggering backtrack for ", combination + letter, ", ",next_digits[1:])
                    backtrack(combination + letter, next_digits[1:])

print(letterCombinations("23"))