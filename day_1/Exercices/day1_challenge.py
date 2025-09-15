# Challenge 1: Multiples of a Number

number = int(input("Enter a number: "))
length = int(input("Enter the length: "))

multiples = [number * i for i in range(1, length + 1)]

print(multiples)

# Challenge 2: Remove Consecutive Duplicate Letters

word = input("Enter a word: ")

result = word[0]

for char in word[1:]:
    if char != result[-1]: 
        result += char

print(result)
