def twoSum(nums, target):
    hashed = {}
    for i in range(len(nums)):
        pair = target - nums[i]
        if nums[i] not in hashed:
            hashed[pair]=i
        else:
            return hashed[nums[i]],i
    return []

twoSum([3,2,4],6)