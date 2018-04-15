def reverseInteger(x):
    pos_x = abs(x)
    reverse = 0 
    while pos_x != 0:
        reminder = pos_x % 10
        reverse = reverse * 10 + reminder
        pos_x = pos_x // 10
    if reverse > pow(2,31):
        return 0
    return reverse if x > 0 else reverse*-1

print reverseInteger(-36485)

# #hacky way
# def reverseInteger2(num):
#     return int(str(num)[::-1])

# print reverseInteger2(47849)



