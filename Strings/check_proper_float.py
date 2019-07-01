def check_if_proper_float(given_f):
    if not given_f or len(given_f)<3:
        return False
    if given_f.count(".")!=1:
        return False
    if given_f.find("-")!=-1 and given_f.index(".") not in [2, len(given_f)-2]:
        return False
    if given_f.index("-")==-1 and given_f.index(".") not in [1, len(given_f)-2]:
        return False
    if given_f.index("-")!=-1 and given_f.index("-")!=0:
        return False
    given_f.replace(".","")
    for c in given_f:
	    if not c.isdigit():
		    return False
    return True

#Test cases
print("1" , check_if_proper_float(None))
print("2", check_if_proper_float(""))
print("3", check_if_proper_float("0"))
print("4", check_if_proper_float(".0"))
print("5", check_if_proper_float("2."))
print("6", check_if_proper_float("-1"))
print("7", check_if_proper_float("-1."))
print("8", check_if_proper_float("-1.1"))
print("9", check_if_proper_float("123.4e2"))
print("10", check_if_proper_float("ee231d"))
print("11", check_if_proper_float(".234.54.7"))
