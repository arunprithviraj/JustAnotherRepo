def gcd(x,y):
    found = False
    count = y
    while not found & count >=2:
        if x%count == 0 and y%count ==0:
            return count
        elif count == 2:
            return 1

        count -=1
