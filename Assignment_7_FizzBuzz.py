
fizzBuzz = []
for i in range(1,101):
    if i%5==0 and i%3==0:
        fizzBuzz.append("FizzBuzz")
    elif i%5==0:
        fizzBuzz.append("Buzz")
    elif i%3 == 0:
        fizzBuzz.append("Fizz")
    else:
        fizzBuzz.append(i)
print(fizzBuzz)