def reverseInteger(num):
    reverse = 0
    while num > 0:
        reminder = num % 10
        reverse = reverse * 10 + reminder
        num = num//10
    return reverse

print reverseInteger(36485)

#hacky way
def reverseInteger2(num):
    return int(str(num)[::-1])

print reverseInteger2(47849)