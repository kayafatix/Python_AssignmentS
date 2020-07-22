sentence = input("Please WRITE a sentence: ")

letter = []
c_number = []

for i in sentence: 
    letter.append(i)
    x=sentence.count(i)
    c_number.append(x)

result = dict(zip(set(letter), c_number))
print(result)