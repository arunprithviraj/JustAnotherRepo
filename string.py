import string

print (string.punctuation)
print (string.ascii_letters)

my_string = "My name is Arun Prithviraj"

lst = my_string.split()

print(lst)

my_string1 = "   Arun    Prith  Raj   "
print (my_string1.strip())

print (my_string1.strip().find("Raj"))

print (my_string1.replace("Arun","Advaith"))
