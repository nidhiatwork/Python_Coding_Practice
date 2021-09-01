def tellSalary():
    usd_inr_rate = 74.26
    type = ['Total', 'Base', 'Stock', 'Bonus']
    for level in [61,62,63,64]:
        print("Level", level,":")
        vals = []
        s = getLevelData(level)
        for line in s.split('\n'):
            if line.startswith('$'):
                line = line.replace(',','')
                vals.append(float(line[1:]))

        for t,val in zip(type,vals):
            print(t,'\t','{:.2f}'.format(val*usd_inr_rate).rjust(20))
        print()

def getLevelData(level):
    s = None
    if level == 61:
        s = '''$49,000\n$33,567\n$11,500\n$3,933'''
    elif level==62:
        s = '''$68,037\nUSD\n$43,370\n$18,111\n$6,556'''
    elif level==63:
        s = '''\n$88,734\n$52,067\n$28,067\n$8,600'''
    elif level==64:
        s = '''$113,500\n$66,500\n$31,750\n$15,250'''
    return s

tellSalary()