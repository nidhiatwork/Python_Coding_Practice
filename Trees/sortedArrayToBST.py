class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if not nums: 
        return None
    mid=len(nums)//2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    print("returning root: ",root.val)
    return root

def sortedArrayToBST_usingIndex(nums):
    # Time: O(n)
    # Space: O(n) in the case of skewed binary tree.
    def convert(left, right):
        if left > right:
            return None
        mid = (left + right + 1) // 2
        root = TreeNode(nums[mid])
        root.left = convert(left, mid-1)
        root.right = convert(mid+1, right)
        print("Returning root: ",root.val)
        return root
    return convert(0, len(nums) - 1)
    
nums = [-10,-3,0,5,9]
print(sortedArrayToBST(nums))
print(sortedArrayToBST_usingIndex(nums))

        