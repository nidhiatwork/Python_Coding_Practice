'''
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
'''

def fizzBuzz_simple(n):
    # ans = ["Fizz" if i%3==0 "Buzz" elif i%5==0 else str(i) for i in range(1,n+1)]
    ans=[]
    for i in range(1,n+1):
        if i%3==0:
            item="Fizz"
        elif i%5==0:
            item="Buzz"
        elif i%15==0:
            item="FizzBuzz"
        else:
            item=str(i)
        ans.append(item)
    return ans

def fizzBuzz_stringConcat(self, n):
    ans = []
    for num in range(1,n+1):
        divisible_by_3 = (num % 3 == 0)
        divisible_by_5 = (num % 5 == 0)
        num_ans_str = ""
        if divisible_by_3:
            # Divides by 3
            num_ans_str += "Fizz"
        if divisible_by_5:
            # Divides by 5
            num_ans_str += "Buzz"
        if not num_ans_str:
            # Not divisible by 3 or 5
            num_ans_str = str(num)

        # Append the current answer str to the ans list
        ans.append(num_ans_str)  

    return ans

def fizzBuzz_Hashmap(self, n):
    ans = []
    fizz_buzz_dict = {3 : "Fizz", 5 : "Buzz"}
    for num in range(1,n+1):
        num_ans_str = ""
        for key in fizz_buzz_dict.keys():
            if num % key == 0:
                num_ans_str += fizz_buzz_dict[key]
        if not num_ans_str:
            num_ans_str = str(num)
        ans.append(num_ans_str)  
    return ans

print(fizzBuzz_simple(15))