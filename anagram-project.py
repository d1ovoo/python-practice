#anagram
import math

word = input('Enter a word:')
while not word.isalpha():
    print("That's not a word")
    word = input('Enter a word:')


letters = list(word.lower())
#print(letters)

numerator = math.factorial(len(letters))
unique_letters = (set(letters))

denominator = 1
for letter in unique_letters:
    count = letters.count(letter) 
    denominator *= math.factorial(count)
    #print(denominator)

anagram = numerator/denominator -1
print(f"There are {int(anagram)} anagrams of that word")









