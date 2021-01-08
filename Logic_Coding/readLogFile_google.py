'''

'''
def readLogsForLogins():
    dict_users=dict()
    success_list=[]
    failures_list=[]
    with open("/Users/nbhushan/OneDrive - Adobe Systems Inc/Nidhi's Folder/N - Personal/Study/Python/Rough/Logic_Coding/log.txt") as f:
        mylist = f.read().splitlines()
        for line in mylist:
            first,last = line.split(":")
            userId_or_status= first.split(" ")[-1].strip()
            if userId_or_status.isdigit(): 
                dict_users[userId_or_status] = last.strip()
            else:
                if first.find("Success")!=-1:
                    success_list.append(last.strip())
                if first.find("Failed")!=-1:
                    failures_list.append(last.strip())
        print("Success:")
        for user in success_list:
            print(dict_users[user])
        print("Failed:")
        for user in failures_list:
            print(dict_users[user])

readLogsForLogins()