# Problem: Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

# -> is a type hint used in func definitions to specify the return type of a function
def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {} # val -> index

# enumerate(nums) iterates over an iterable while keeping track of the index and the value.
# removes the need to manually maintain a counter
    for i, num in enumerate(nums):
        complement = target - num # calculates the value needed to add up to the target
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []

nums = 1,2,3,4,7;
target = 8;
print(twoSum(nums,target))