def reverseInteger(x):
    reverse = 0 
    if x>0:
        while x != 0:
            reminder = x % 10
            reverse = reverse * 10 + reminder
            x = x // 10
        if reverse > pow(2,31):
            return 0
        else:
            return reverse
    elif x<0:
        x = -1*x
        while x != 0:
            reminder = x % 10
            reverse = reverse * 10 + reminder
            x = x // 10
        if reverse > pow(2,31):
            return 0
        else:
            return -1 * reverse
    else:
        return 0

print reverseInteger(-36485)

# #hacky way
# def reverseInteger2(num):
#     return int(str(num)[::-1])

# print reverseInteger2(47849)