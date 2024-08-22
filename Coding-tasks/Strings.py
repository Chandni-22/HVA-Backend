'''1.) Count Vowels and Consonants: You are given a String. Count the number of vowels and consonants the string has. Print the number of vowels followed by the number of consonants.
Note: The string may contain other character like space and full stop.

Vowels are alphabets belonging to the following group - {a, e, i, o u}. Consonants are rest of the alphabets that do not belong to the group - {a, e, i, o u}.

Sample Input: 
Hello World
Sample Output: 
3 7
Explanation: The string has 3 vowels and 7 consonants.'''

# str=input("Write a sentance: ")
# str=str.lower()
# l=len(str)
# i,vowels,consonants=0,0,0
# while i<l:
#     if (str[i]=="a") or (str[i]=="e") or (str[i]=="i") or (str[i]=="o") or (str[i]=="u"):
#         vowels+=1
#     elif "a"<=str[i]<="z":
#         consonants+=1
#     i+=1
# print(vowels,consonants)


'''2.) Character Count in a String: You are given a String and a Character. Count how many times the Character is present in the given String. If the Character is not present in the String, print "No".

Sample Input 1: 
Hello World
l
Sample Output 1: 
3
Explanation 1: The Character l is present 3 times in the String "Hello World".

Sample Input 2: 
Hello World
a
Sample Output 2: 
No
Explanation 2: The Character a is not present in the String "Hello World".'''

# str=input("Write a sentance: ")
# character=input("Enter the character: ")

'''Way 1:'''
# l=len(str)
# i,Count=0,0
# while i<l:
#     if character==str[i]:
#         Count+=1
#     i+=1
# if Count>0:
#     print(Count)
# else:
#     print("No")    

'''Way 2:'''
# if character in str:
#     print(str.count(character))
# else:
#     print("No")


'''3.) Check for Anagram: You are given two String S1 and S2. Determine if the two strings are anagrams of each other.
Note: You will have to ignore case and white spaces.

Anagrams are words or phrases formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. For example, the word "listen" is an anagram of "silent".

Sample Input 1: 
Silent
Listen
Sample Output 1: 
Yes
Explanation 1: Silent and Listen has the same letters. If we ignore case, they are anagrams.

Sample Input 2: 
New York Times
monkeys write
Sample Output 2: 
Yes
Explanation 2: If we don't consider white space and case-sensitive, "New York Times" and "monkeys write" are anagrams. They have same characters repeating same number of times.'''

# str_1=input("Enter first string: ")
# str_2=input("Enter second string: ")
# s_1=str_1.lower()
# s_2=str_2.lower()
# str_1=sorted(s_1.replace(" ",""))
# str_2=sorted(s_2.replace(" ",""))
# ans="Yes" if str_1==str_2 else "No"
# print(ans)


'''4.) Remove Duplicate Characters: You are given a string. Create a new string that contains each character of the original string only once, preserving the order of their first occurrences.

Sample Input: 
programming
Sample Output: 
progamin
Explanation: We print a new string removing the repeating characters. R, m and g were repeating in the given string "programming" and hence were removed from the new string.'''

# str=input("Enter a string: ")
# main=""
# i=0
# while i<(len(str)):
#     if main.count(str[i])==0:
#         main+=str[i]
#     i+=1
# print(main)


'''5.) Capitalize nth Character: You are given a String and and an index. Capitalize the character at the nth position in the given String.
Note: You can consider the index to start from 0.

Sample Input: 
programming
6
Sample Output: 
prograMming'''

# str=input("Enter a string: ")
# n=int(input("Enter a number: "))

'''Way 1:'''
# ans=str[:n]+str[n].upper()+str[n+1:]
# print(ans)

'''Way 2:'''
# a=str.replace(str[n],str[n].upper(),1)
# print(a)


'''6.) Password Validator: Write a program that takes a string S as input and checks if the string S satisfies all the following conditions to be a strong password:
a.) Contains at least 8 characters.
b.) Contains at least one lowercase character.
c.) Contains at least one uppercase character.
d.) Contains at least one number.
e.) Contains at least one special character.
If the string S satisfies all conditions, print yes, else print no.

Sample Input 1: 
Abcd@123
Sample Output 1: 
Yes

Sample Input 2: 
Xyz123
Sample Output 2: 
No'''

# sc="!@#$%^&*()-=_+.,<>"

# password=input("Enter password: ")
# space=password.replace(" ","")
# l=len(password)
# if (password==space) and (l>=8):
#     i=0
#     count_cap,count_low,count_number,count_spe=0,0,0,0
#     while i<l:
#         if "A"<=(password[i])<="Z":
#            count_cap+=1
#         elif "a"<=(password[i])<="z":
#            count_low+=1
#         elif "0"<=(password[i])<="9":
#            count_number+=1   
#         elif (password[i]=="!") or (password[i]=="@") or (password[i]=="#") or (password[i]=="$") or (password[i]=="%") or (password[i]=="^") or (password[i]=="&") or (password[i]=="*") or (password[i]=="(") or (password[i]==")") or (password[i]=="-") or (password[i]=="_") or (password[i]=="+") or (password[i]=="=") or (password[i]=="<") or (password[i]==">") or (password[i]==".") or (password[i]==","):
#            count_spe+=1
#         i+=1
#     if count_cap>0 and count_low>0 and count_number>0 and count_spe>0:
#         print("Yes")      
# else:
#   print("No")


'''7.) Search Character in a String: You are given a string S. You are also given a character c. Check if the character c is present in the string S. If present print yes, else print no.

Sample Input 1:
abcdefgh
f
Sample Output 1:
Yes

Sample Input 2:
abcdefgh
r
Sample Output 2:
No'''

# str=input("Write a sentance: ")
# character=input("Enter the character: ")

'''Way 1:'''
# i,Count=0,0
# while i<(len(str)):
#     if str[i]==character:
#         Count+=1
#         break
#     i+=1
# if Count>0:
#     print("Yes")
# else:
#     print("No")

'''Way 2:'''
# a=str.find(character)
# ans="Yes" if a>=0 else "No"
# print(ans)


'''8.) Search Word in a Sentence: You are given a sentence S. You are also given a word W. Check if the word W is present in the sentence S. If present print yes, else print no.
The input word W will have no space in between.

Sample Input 1:
How are you doing today?
today
Sample Output 1:
Yes

Sample Input 2:
How are you doing today?
do
Sample Output 2:
No
'''