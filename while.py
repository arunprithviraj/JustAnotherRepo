lst=[[True,1,2,3,4,5],[True,True,True,False],[1,1,1,0,0,1]]
for i in lst:
    var = 1
    sum1 = 0
    
    while i[0] and var < len(i):
        sum1 += i[var]
        var  += 1
    print (sum1)
    
    
