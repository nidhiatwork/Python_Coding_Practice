import pickle
data1 = [ { 'a':'A', 'b':2, 'c':3.0 } ] 
print('BEFORE:')
print(data1)
data1_string = pickle.dumps(data1) 
data2 = pickle.loads(data1_string) 
print('AFTER:')
print(data2)
print('SAME?:', (data1 is data2))
print('EQUAL?:', (data1 == data2))