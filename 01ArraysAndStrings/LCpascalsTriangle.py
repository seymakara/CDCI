# Example:

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
class Solution(object):
    def generate(self, numRows):
        listOfRows = []
        for i in range(numRows):
            listOfRows.append([1]*(i+1)) #creastes the list of rows including the items as many as the number of the row
            if i>1: #start from the third row. You don't need to change anything for the first two lines.
                for j in range(1,i): # the first and the last items are 1. So exclude them.
                    listOfRows[i][j]=listOfRows[i-1][j-1]+listOfRows[i-1][j] # bir rakamin toplami ondan onceki siradaki onla ayni hizadaki ve ondan bi onceki hizadaki rakamin toplamina esittir..
        return listOfRows