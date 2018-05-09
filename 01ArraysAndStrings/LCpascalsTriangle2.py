# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

# Note that the row index starts from 0.

class Solution(object):
    def getRow(self, rowIndex):
        listOfRows = []
        for i in range(rowIndex+1):
            listOfRows.append([1]*(i+1)) #creastes the list of rows including the items as many as the number of the row
            if i>1: #start from the third row. You don't need to change anything for the first two lines.
                for j in range(1,i): # the first and the last items are 1. So exclude them.
                    listOfRows[i][j]=listOfRows[i-1][j-1]+listOfRows[i-1][j] # bir rakamin toplami ondan onceki siradaki onla ayni hizadaki ve ondan bi onceki hizadaki rakamin toplamina esittir..
        return listOfRows[-1]