def hammingWeight(n):
    counter = 0
    print bin(n)
    for item in bin(n):
        print item
        
        if item == "1":
            print "counter", counter
            counter += 1
    return counter
print hammingWeight(3)
