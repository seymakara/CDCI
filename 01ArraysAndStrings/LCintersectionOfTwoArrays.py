# Given two arrays, write a function to compute their intersection.

# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

# _______SORTED LIST SOLUTIOON______
class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        
        pointer1 = 0
        pointer2 = 0
        res = []
        
        while pointer1 < len(nums1) and pointer2 < len(nums2):
            if nums1[pointer1] > nums2[pointer2]:
                print "hello1"
                pointer2 += 1
            elif nums1[pointer1] < nums2[pointer2]:
                print "hello2"
                pointer1 += 1
            else:
                print "hello3"
                res.append(nums1[pointer1])
                pointer1 += 1
                pointer2 += 1
        return res

    #_______HASHMAP SOLUTION________

    class Solution(object):
    def intersect(self, nums1, nums2):
        dict = {}
        res = []
        
        if len(nums1) > len(nums2):
            big = nums1
            small = nums2
        big = nums2
        small = nums1
        
        for num in small:
            dict[num] = dict.get(num, 0) + 1
        
        for num in big:
            if num in dict and dict[num] > 0:
                res.append(num)
                dict[num] -=1
        return res