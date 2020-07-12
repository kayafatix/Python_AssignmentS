number = int(input("Please enter a positive number:  "))
if number == 0:
    print(f"{number} is not a prime number!")
elif number == 1:
    print(f"{number} is not a prime number")
else:
    for i in range(2, number):
        if number % i == 0:
            print(
                f"{number} is not prime number. \n***** '{i}' is divider of {number}*****"
            )
            break
    else:
        print(f"{number} is prime number!!")
