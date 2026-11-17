# Practice set

# reverse name 
name = input("Enter your name : ")

print(name[::-1])


# Count Characters 
sentence = input("Enter a sentence : ")

print(sentence.count('o'))


# convert to uppercase and lowercase
word = input("Enter a word : ")

print(word.upper())
print(word.lower())


# palindrome 
word1 = input("Enter a word : ")

if word1 == word1[::-1]:
    print("It is a Palindrome")
else : 
    print("It is not a Palindrom")


# counting particular character
name1 = input("Enter your name ; ")
letter = input("Entyer a letter to count : ")

print(name1.count(letter))
 
 
# Count Vowels
name2 = input("Enter your name : ")
name2 = name2.lower()

vowels = "aeiou"

count = (
    name2.count('a')+
    name2.count('e')+
    name2.count('i')+
    name2.count('o')+
    name2.count('u')
)

print("Total number of vowels : " , count)