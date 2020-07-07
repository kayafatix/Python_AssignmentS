# Takes the first name from the user and compares it to yours,
# Then if the name the user entered is the same as yours, print out such as : "Hello, Joseph! The password is : W@12",
# If the name the user entered is not the same as yours, print out such as : "Hello, Amina! See you later."

first_name = "Joseph" 
first_name1 = input("Please ENTER your first name: ")

if first_name == first_name1:
    print(f"Hello, {first_name1}! The password is : W@12")
else:
    print(f"Hello, {first_name1}! See you later.")
    