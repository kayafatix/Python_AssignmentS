
age = input("Are you a cigarette addict older than 75 years old?: ") == "yes"
chronic = input("Do you have a severe chronic disease?: ") == "yes"
immune = input("Is your immune system too weak?: ") == "yes"

#print(age, chronic, immune)
risk = (age or chronic or immune)

if risk == True:
    print("You are in risky group")
else:
    print("You are not in risky group")
