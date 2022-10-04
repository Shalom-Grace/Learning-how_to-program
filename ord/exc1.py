#!/usr/bin/python3
print("This is an Acronym Generator")
#the acronym is generated from first letter of each words
str_name = input("Please enter the word you want to generate acronym from: ")
str_name = str_name.upper()
list_of_words = str_name.split()
for word in list_of_words:
    print(word[0], end="")
print()

#the acronym is generated from first 3 letters of each word
orig_name = input("Convert to acronym: ")
orig_name = orig_name.upper()
list_of_words = orig_name.split()
for word in list_of_words:
    print(word[:3], end="")
print()