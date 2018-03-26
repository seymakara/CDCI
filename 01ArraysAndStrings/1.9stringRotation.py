# input = cellphone, input2 = honecellp
# input1 is a substring of input1
# to check this duplicate input1 as cellphonecellphone
# check if input2 is in input1

def stringRotation(input1, input2):
    if len(input1) == len(input2) and len(input1) != 0:
        newStr = input1 + input1
        if input2 in newStr:
            return True
        return False
    return False

print stringRotation("cellphone", "honecellp")