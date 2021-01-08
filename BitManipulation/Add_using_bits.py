'''Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
'''
def Add_using_bits(a, b): 
        if (b <= 0):
            return a
        else:
            return Add_using_bits(a ^ b, (a & b) << 1)
  
print(Add_using_bits(-1, 1))

