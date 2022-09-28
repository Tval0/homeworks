


your_name = str(input("enter your name: " ))
your_surname = str(input("enter your surname: " ))
your_age = int(input("enter your age: " ))
your_location = str(input("enter your location: " ))
your_hobby = str(input("enter your hobby: " ))
your_height= int(input("enter your height "))
question= str(input("do you have pet "))


if question=="yes":
    print("what kind of pet")
    x=str(input())

    print("my name is " , your_name, "my surename is " ,your_surname,"i am " , your_age, "years old","i am from ",  your_location , "my hobby is ",  your_hobby,"i am ",  your_height,"cm tall",
     " and i have " ,x)




elif question=="no":  
    print("my name is " , your_name, "my surename is " , your_surname,"i am " , your_age, "years old","i am from " , your_location , "my hobby is " , your_hobby,"and i am " , your_height,"cm tall")
 













