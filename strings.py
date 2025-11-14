import re        #used in question 6





"""
1.Write a Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.
Sample function and result :
first_three('ipy') -> ipy
first_three('python') -> pyt

"""
word = "python"

def slicing(word):
    return word[0:3]  # we are slicing letters from the word the third index is excluded

print(slicing(word))

"""
2.Write a Python program to create a Caesar encryption.
->swapping a character for another
->a key determines the number of positions each letter is shifted

     -parameters should be a string and a key
     -for every word to be shifted we should use a loop
     -in the loop every character should be moved (key) times in the alphabet.



"""

word = "murder"

def cipher (word,key):
    output = ""
    for char in word:  #loops each character
        if 'a' <= char <= 'z' : # handles lowercase
            output += chr(((ord(char)-ord('a')+key) % 26) + ord('a')) # ord(char) gets the ASCII char value
        elif 'A' <= char <= 'Z' : # handles uppercase
            output += chr(((ord(char)-ord('A')+key) % 26) + ord('A')) #chr(...) converts ASCII to character
        else: #non-alphabetic characters
            output += char
    return output

print(cipher(word,3))


"""
3. Write a Python program to remove duplicate characters from a given string.
   ->access duplicates using indexing
   ->loop through the string
   ->.replace() replaces all occurrences of a specified char with another
   ->we will replace the character with nothing hence an empty string
"""
word = "bodaaccious"
letter = "a" 

def rm_duplicate(word,letter):
    return word.replace(letter,"",1) #1 is a count argument

print(rm_duplicate(word,letter))


"""
4.Write a Python program to delete all occurrences of a specified character in a given string.
"""
word = "tyson yarn python"
letter = "y"
def delete (word ,letter):
    return word.translate(word.maketrans("","",letter))

print(delete(word,letter))



"""
5.Write a Python program that counts the number of leap years within the range of years. Ranges of years should be accepted as strings.

"""
string = "2000-2020"


def leap(string):
    count = 0
    start, end = map(int, string.split('-'))
    for year in range(start, end + 1): # the +1 is used so as to include 2020 in the loop
        if (year % 400 == 0):
            count += 1
    return (f"{count} leap years")

print(leap(string))



"""
6.Write a Python program to insert space before every capital letter appears in a given word
"""
word= "PythonExercisesPracticeSolution"

def spacing (word):
     
    return re.sub(r"(\w)([A-Z])", r"\1 \2", word)

print(spacing(word))
