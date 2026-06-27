print("Welcome to the Interactive Personal Data Collector! \n")

name=input("Please enter your name:")
age=int(input("Please enter your age"))
height=float(input("Please enter your height in meters"))
favnum=int(input("Please enter your favorite number"))

print("\n Thank you! Here is the information we collected:\n")

print("Name",name,"(Type",type(name),"Memory Address:",id(name),")")
print("Age",age,"(Type",type(age),"Memory Address:",id(age),")")
print("Height",height,"(Type",type(height),"Memory Address:",id(height),")")
print("Fav number",favnum,"(Type",type(favnum),"Memory Address:",id(favnum),")")

print("\n")
currentyear=2026
birthyear=currentyear-int(age)

print("\n Your birth year is approximately :\n")
print(birthyear,"(based on your age of)",age)

print("\n Thank you for using the personal Data Collector. Goodbye!")