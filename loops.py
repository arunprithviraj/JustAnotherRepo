lst = ["one","three","two"]
for i in lst:
    print(i)

#for i in range(0,len(lst)):
#    print(lst[i])
 #   lst[i] = "gorrila"
  #  print (lst)

for i in range(0,len(lst)):
    print ("* " + lst[i])
    print(i)
    for j in range(0,i):
        print ("#"+lst[j])
    
