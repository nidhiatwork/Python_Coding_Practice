def find_Kth_Smallest(given_list, k):
    if not given_list or k>len(given_list):
        return -1
    sorted_list = selection_sort(given_list)
    print(sorted_list)
    return sorted_list[k-1]

def selection_sort(given_list):
    for i in range(len(given_list)):
        for j in range(i+1, len(given_list)):
            print(i,j)
            if given_list[i]>given_list[j]:
                max_index = i
            else:
                max_index = j
            print("Max: ", max_index)
        if max_index==i:
            given_list[j],given_list[i] = given_list[i],given_list[j]
            print("Swap done!: {}".format(given_list))
    return given_list

print(find_Kth_Smallest([3,23,6,20,76,25,2],3))