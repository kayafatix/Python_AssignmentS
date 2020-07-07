"""Find out the most frequent number and its frequency.
Write a program that;
Finds out the most frequent number in the given list.
Calculates its frequency."""

numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
#numbers.sort()
a = max(numbers, key=numbers.count)
b = numbers.count(a)
print(a)
print(b)
#most_number = numbers.count(3)
#print(f"the most frequent number is {most_number} and it was {most_number} times repeated.")
