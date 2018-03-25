# 1. count the number of chars with for loop
# 2. when char changes:
    # previous char + count
    # count = 0
# 5. if str. length < new string
    # return new string
def stringCompression(input):
    count = 0
    newString = ""
    for i in range(len(input)):
        count += 1
        if i+1 >= len(input) or input[i] != input[i+1] :
            newString += input[i] + str(count)
            count = 0
    if newString > input:
        return input
    return newString

print stringCompression("aaabbksfurydccccaa")