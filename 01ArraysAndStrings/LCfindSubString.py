class Solution(object):
    def strStr(self, haystack, needle):
        hayLen = len(haystack)
        needleLen = len(needle)
        
        if needleLen == 0:
            return 0
        
        for hayIndex in range(hayLen - needleLen +1): #no deed to check all of the string. needle uzunlugundan bir fazla kisminda yoksa kalan kisimda da yoktur
            for needleIndex in range(needleLen):
                if haystack[hayIndex+needleIndex] != needle[needleIndex]: # if it is equal we need to increment both index, that's why we add needleIndex to hayIndex
                    break
                if needleIndex == needleLen -1: #if needleIndex reaches to the end it means we found the needle in the hay
                    return hayIndex
        return -1