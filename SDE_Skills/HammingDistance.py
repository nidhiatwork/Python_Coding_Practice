


def hammingDistance(x, y):
        return bin(x^y).count('1')

#Time complexity: Log(x)+N
print(hammingDistance(2,4))