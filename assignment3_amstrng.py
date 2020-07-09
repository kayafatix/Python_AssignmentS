number = input("Please, TYPE a positive integer number: ")
number_li=list(number)

while not number.isdigit():
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    number = input("TYPE a positive integer number: ")
    number_li=list(number)
if  number.isdigit():
    j = len(number_li) 
    n_digit = 0
    for i in range(len(number)):
        k = int(number_li[i])**j 
        n_digit += k
    if n_digit == int(number):

        print(f"{n_digit} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number because the result is {n_digit}.")