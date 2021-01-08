'''Shuffle a set of numbers without duplicates.'''
import random
class Solution:
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    # Fisher Yates Algo
    # Pick any random index between i and the last index and swap i and that random idx. Repeat for every possible i.
    def shuffle(self):
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array

nums = [1, 2, 3, 4]
obj = Solution(nums)
new = obj.shuffle()
print(new)
