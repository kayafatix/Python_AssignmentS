print("*****   if your answer is 'Yes'; Please enter '1' ; if your answer 'No'; Please enter '0'   *****")
age = int(input("Are you a cigarette addict older than 75 years old? (Yes: 1; No :0): "))
chronic = int(input("Do you have a severe chronic disease?  (Yes: 1; No :0):  "))
immune = int(input("Is your immune system too weak? (Yes: 1; No :0): "))
risk = bool((age or chronic )  and  (age or immune)  and (immune or chronic)) 

print(f"Your result is: {risk}") 
print("İf your result is 'True' there is a risk of death!")
print("İf your result is 'False' there is not a risk of death!")