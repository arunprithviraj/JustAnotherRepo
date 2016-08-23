atuple = (("Arun","Prithviraj",34,"M"),("Seethu","Satheesh",31,"F"), \
          ("Advaith","Arun",5,"M"))
#print (atuple)

f_name = ""
l_name = ""
age = ""
gender = ""

for i in atuple:
    f_name,l_name,age,gender = i
    print f_name,l_name,age,gender
