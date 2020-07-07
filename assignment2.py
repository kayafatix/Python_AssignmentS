
age = input("Are you a cigarette addict older than 75 years old?: ")
chronic = input("Do you have a severe chronic disease?: ")
immune = input("Is your immune system too weak?: ")

if age == "no" and chronic=="no" and immune=="no":
    print("there is not a risk of death")
elif age =="yes" or chronic == "yes" or immune == "yes":
    print("there is a risk of death")
else:
    print("there is a risk of death")