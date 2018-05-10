# bruteforce solution n2
def twoSum(nums, target):
    for i in range(len(nums)-1):
        for j in range(1, len(nums)-1):
            if nums[i] + nums[j] == target:
                return [i,j]
            else:
                j += 1
        i += 1

# hash map solution
def twoSumHash(nums, target):
    newHash = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in newHash:
            return [i, complement]
        newHash[nums[i]] = 1