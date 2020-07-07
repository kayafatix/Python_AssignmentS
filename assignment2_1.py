age = input ("Are you a cigarette addict older than 75 years old? (Yes or No) = ")
chronic = input ("Do you have a severe chronic disease?  (Yes or No) = ")
immune = input("Is your immune system too weak? (Yes or No)= ")
risk = (age or chronic) and (age or immune) and (chronic or immune)
risk_durumu = risk=="yes"
print(risk_durumu, '\n'+ "(True means there is a risk of death)" +'\n'+ "(False means there is not a risk of death)")