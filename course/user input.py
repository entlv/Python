# i want to be a software engneer :
#==========================================================================================================[user input]
name= str(input("what is tour name"))
age=int(input(" enter your age ")) 
#or 
age=int(age) # to coverset in to int not str
age +=1
print("HAPPY BIRTDAY!")
print("hello,my name is",name ,"I'm", age, "years old. nice to met you ")
#==================================[Exercise 1( rectangle area calcater)]
h=int(input("Enter the rerectangle's hight: "))
w=int(input("Enter the rerectangle's wigth: "))
area=h*w
#print(area)
#function
def rectangle_area(h,l):
    print(f"rectangle area is : {h*l}")
rectangle_area(h,w)
