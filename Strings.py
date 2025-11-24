# Check if the given String is Palindrome or not
def palindrome(s):
    s = s.lower()  # Convert to lowercase
    n = len(s)
    i = 0
    j = n - 1

    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True 

# Test
s = "QABCDCBAq"
if palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")



#Count number of vowels, consonants, spaces in String------------------------------------------------
def count_chars(s):
    consonants = 0
    vowels = 0
    spaces = 0
    
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    
    for char in s.lower():  # Convert to lowercase for uniformity
        if char in vowels_list:
            vowels += 1
        elif char == " ":
            spaces += 1
        elif char.isalpha() and char not in vowels_list:
            consonants += 1
        # Ignore digits or special characters
    
    return consonants, vowels, spaces

# Test
consonants, vowels, spaces = count_chars("Take u to the next level")
print(f"Consonants: {consonants}\nVowels: {vowels}\nSpaces: {spaces}")


# Find ASCII value of a character---------------------------------------------
char = 'A'
ascii_value = ord(char)
print(f"ASCII value of '{char}' is {ascii_value}")

# Remove all vowels from the String-------------------------------------------

def remove_vowels(s):
    s = s.lower()
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    new_str = ""
    
    for char in s:
        if char not in vowels_list:
            new_str += char
    return new_str

# Test
s = "Godzilla is coming"
print(remove_vowels(s))


# Remove Spaces from a String----------------------------

def remove_space(s):
    s = s.lower()
    new_str = ""
    for char in s:
        if char != " ":
            new_str+=char
    return new_str

# Test
s = "Godzilla is coming"
print(remove_space(s))

# Remove characters from a string except alphabet----------------------------

def remove_characters(s):
    s = s.lower()
    new_str = ""
    for char in s:
        if char.isalpha():
            new_str+=char
    return new_str

# Test
s = "Godzilla2 #Yu is coming34Po*p"
print(remove_characters(s))


# Reverse a String--------------------------------------

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


s = "Yash"
print(reverse_string(s))


# Remove brackets from an algebraic expression----------------------------

def remove_brackets(s):
    new_str = ""
    for char in s:
        if char != "(" and char != ")":
            new_str += char
    return new_str


s = "(((a-b))+c)"
print(remove_brackets(s))


# Sum of the Numbers in a String----------------------------


def add_num(s):
    total = 0
    for char in s:
        if char.isdigit():
            total += int(char)
    return total


s = "123xyz"
print(add_num(s))

# Capitalize first and last character of each word of a string----------------------------


def Capitalize(s):
    s = list(s)  # Convert string to list for mutability
    n = len(s)
    
    # Capitalize first and last character
    s[0] = s[0].upper()
    s[n-1] = s[n-1].upper()
    
    for i in range(n):
        if s[i] == " ":
            s[i-1] = s[i-1].upper()  # Last char of previous word
            s[i+1] = s[i+1].upper()  # First char of next word
    
    return ''.join(s)  # Convert back to string

# Test
s = "this is correct that is godzilla"
print(Capitalize(s))

# Calculate Frequency of characters in a Stringg----------------------------

def frequency(str):
    freq={}
    visit=[]
    for char in str:
        if char!=" ":
            if char not in visit:
                visit.append(char)
                freq[char]=1
            else:
                freq[char]+=1
        
    return freq
    
str="Man is man is good on earth"
print(frequency(str))


# Find Non-repeating characters of a String--------------------------------------

def nonRepetitive(string):
    string = string.lower()
    result = ""
    for char in string:
        if string.count(char) == 1 and char != " ":
            result += char
    return result
 
string = "Google Pro Parrtor"
print(nonRepetitive(string)) 

# Check if two Strings are anagrams of each other------------------------

def anagram(a,b):
    return sorted(a.lower())==sorted(b.lower())


# heck if two strings match where one string contains wildcard charactersr------------------------

import fnmatch

def wildcard_match(pattern, string):
    return fnmatch.fnmatch(string, pattern)

# Example usage:
print(wildcard_match("a?c", "abc"))      # True
print(wildcard_match("a*c", "abbbc"))    # True
print(wildcard_match("a*c", "ac"))       # True
print(wildcard_match("a*c", "ab"))       # False

a,b="CATg", "ACtg"
if anagram(a,b):
    print("Anagram")
else:
    print("Not anagram")


# Maximum occurring character in a string-------------------
def maxOcc(string):
    freq={}
    for char in string:
        if char!=" ":
            if char not in freq:
                freq[char]=1
            else:
                freq[char]+=1
    
  # Find the character with maximum frequency
    max_char = max(freq, key=freq.get)
    return max_char, freq[max_char]

        
    
string="Hello pelooow"
print(maxOcc(string))

# Remove All Duplicates from a String-------------------

def removeDuplicates(string):
    seen = set()
    newStr = ""
    for char in string.lower():  # case-insensitive
        if char.isalpha() and char not in seen:
            seen.add(char)
            newStr += char
    return newStr

string = "Godzilla is back"
print(removeDuplicates(string))  # Output: "godzilabck"


# Print all the duplicates in the string--------------------

def duplicates(str):
    freq={}
    for char in str:
        if char not in freq:
            freq[char]=1
        else:
            freq[char]+=1
            
    duplicate_str={}
    for key in freq:
        if freq[key]>1:
            duplicate_str[key]=freq[key]
            
    return duplicate_str
        
    
    
str= "sinstriiintng"
print(duplicates(str))

# Remove Characters from first String present in the Second String--------------


def removeChar(str1, str2):
    result = ""
    for char in str1:
        if char not in str2:
            result += char
    return result

str1 = "abcdef"
str2 = "cefz"
print(removeChar(str1, str2))  

# Change every letter with next lexicographic alphabet---------------------------
#Input: str1 = “xyzpw”, str2 = "lmno" 
# Output: xyzpw 

def lexicographic(s):
    result=""
    for char in s:
        if char.isalpha():
             #Shift character by 1, wrap around after 'z'
             if char =='z':
                 result+='a'
             elif char=="Z":
                 result+="A"
             else:
                result+=chr(ord(char)+1)
        else:
            result+=char
    return result 

str1 = "xyzpw"
print(lexicographic(str1))  # Output: yz


# Find the largest word in a String--------------------------------

def largestWord(str):
    LargestWord=""
    word_list=str.split(" ")
    currLen=len(word_list[0])
    for word in word_list:
        if len(word)>currLen:
            LargestWord=word
            currLen=len(word)
    return LargestWord
    
    
str="Google is the large company in this universe pokimonPro is good"
print(largestWord(str))

            



            


