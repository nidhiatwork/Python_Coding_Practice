

def recommend(file, price, cuisines_list):
    name_to_rating,price_to_names,cuisine_to_names = read_restuarants(file)
    names_matching_price = price_to_names[price]
    final_list={}
    for cuisine in cuisines_list:
        rests = cuisine_to_names[cuisine]
        for rest in rests:
            if rest in names_matching_price:
                final_list[rest] = name_to_rating[rest]
    print(sorted(final_list.items(), reverse=False))
    # print(final_list.items())

def read_restuarants(file):
    name_to_rating={}
    price_to_names={'$':[],'$$':[],'$$$':[], '$$$$':[]}
    cuisine_to_names={}
    i=1
    with open(file) as f:
        contents = f.readlines()
        for line in contents:
            if line.strip():
                l = line.strip()
                if i ==1:
                    rest_name = l
                if i ==2:
                    rating=l
                    name_to_rating[rest_name]=rating
                if i==3:
                    price=l
                    price_to_names[l].append(rest_name)
                if i==4:
                    cuisine_list = l.split(',')
                    for cuisine in cuisine_list:
                        if cuisine not in cuisine_to_names.keys():
                            cuisine_to_names[cuisine] = [rest_name]
                        else:
                            cuisine_to_names[cuisine].append(rest_name)
            else:
                i=0
            i=i+1
        return name_to_rating,price_to_names,cuisine_to_names
            
if __name__=="__main__":
    recommend('data.txt','$',['Chinese'])