'''
We have some clickstream data that we gathered on our client's website. We collected snippets of users' anonymized URL histories while they browsed the site. The histories are in chronological order, and no URL was visited more than once per person.

Write a function that takes two users' browsing histories as input and returns the longest contiguous sequence of URLs that appears in both.

Sample input:

user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]
user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]

Sample output:

findContiguousHistory(user0, user1) => ["/pink", "/register", "/orange"]
findContiguousHistory(user0, user2) => [] (empty)
findContiguousHistory(user0, user0) => ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
findContiguousHistory(user2, user1) => ["a"] 
findContiguousHistory(user5, user2) => ["a"]
findContiguousHistory(user3, user4) => ["/plum", "/blue", "/tan", "/red"]
findContiguousHistory(user4, user3) => ["/plum", "/blue", "/tan", "/red"]
findContiguousHistory(user3, user6) => ["/tan", "/red", "/amber"]
findContiguousHistory(user6, user3) => ["/tan", "/red", "/amber"]

n: length of the first user's browsing history
m: length of the second user's browsing history
'''
def findContiguousHistory(user1, user2):
    hmap = dict()
    for i,val in enumerate(user1):
        hmap[val]=i
    
    longest=[]
    current=[]
    for item in user2:
        if item in hmap:
            if not current:
                current.append(item)
            elif hmap[item]-hmap[current[-1]]==1:
                current.append(item)
            else:
                current = [item]
            if len(current)>len(longest):
                longest=current
        else:
            current=[]
    return longest


user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]
user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]

print(findContiguousHistory(user0, user1)) # Output: ["/pink", "/register", "/orange"]
print(findContiguousHistory(user0, user2)) # Output: []
print(findContiguousHistory(user0, user0)) # Output: ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
print(findContiguousHistory(user2, user1)) # Output: ["a"]
print(findContiguousHistory(user5, user2)) # Output: ["a"]
print(findContiguousHistory(user3, user4)) # Output: ["/plum", "/blue", "/tan", "/red"]
print(findContiguousHistory(user4, user3)) # Output: ["/plum", "/blue", "/tan", "/red"]
print(findContiguousHistory(user3, user6)) # Output: ["/tan", "/red", "/amber"]
print(findContiguousHistory(user6, user3)) # Output: ["/tan", "/red", "/amber"]
