'''In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
'''

from collections import Counter
def totalFruit(tree):
    ws = 0
    ans = 0
    counter = Counter()
    for we in range(len(tree)):
        counter[tree[we]]+=1
        while len(counter)>=3:
            if tree[ws] in counter:
                counter[tree[ws]]-=1
                if counter[tree[ws]]==0:
                    del counter[tree[ws]]
                ws+=1
        ans = max(ans, we-ws+1)
    return ans

tree = [3,3,3,1,2,1,1,2,3,3,4]
print(totalFruit(tree))