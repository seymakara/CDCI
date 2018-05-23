# Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

# Please note that the string does not contain any non-printable characters.

# Example:

# Input: "Hello, my name is John"
# Output: 5

class Solution(object):
    def countSegments(self, s):
        segment_count = 0 
        for i in range(len(s)):
            if (i == 0 or s[i-1] == " ") and s[i] != " ": # s[i-1] == " " and s[i] != " " this prevents these inputs ("        ") to return.
                segment_count += 1
                print segment_count
        return segment_count