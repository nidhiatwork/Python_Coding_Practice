
import re

a = "nidhi bhushan"
pattern = "[\S]"
a = re.findall(pattern,a)
print(a)