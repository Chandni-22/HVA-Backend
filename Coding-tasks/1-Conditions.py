'''1.) Odd or Even: Write a program that takes a positive integer n as input and prints whether it is odd or even.

Sample Input 1: 
49
Sample Output 1: 
Odd
Sample Input 2: 
36
Sample Output 2: 
Even
'''
# n=int(input("Enter number: "))
# ans="Even" if n%2==0 else "Odd"
# print(ans)


'''2.) Grading System: Write a program that takes a student's score (out of 100) and outputs their grade based on the following conditions:

90-100: Grade A
80-89: Grade B
70-79: Grade C
60-69: Grade D
Below 60: Grade F

Sample Input 1: 
78
Sample Output 1: 
C
Sample Input 2: 
90
Sample Output 2: 
A
Sample Input 3: 
48
Sample Output 3: 
F
'''
# score = int(input("Enter the student's score (out of 100): "))
# if 0<=score<=100:
#     if score>=90:    
#         grade="A"
#     elif score>=80:
#         grade="B"
#     elif score>=70:
#         grade="C"
#     elif score>=60:
#         grade="D"
#     elif score>=0:
#         grade="F"
# else:
#     grade="Invalid score!"
# print(grade)

 
'''3.) Age Group Categorizer: Write a program that categorizes a person's age into different life stages based on the following conditions:

0-2 years: Infant
3-12 years: Child
13-19 years: Teenager
20-65 years: Adult
Above 65 years: Senior

The program takes an age as input and prints the age group category the person belongs to. 
Sample Input 1:
15
Sample Output 1:
Teenager
Sample Input 2: 
2
Sample Output 2: 
Infant
Sample Input 3: 
72
Sample Output 3: 
Senior
'''
# age=int(input("Enter age: "))
# if age>0:
#     if age<=2:
#         ans="Infant"
#     elif age<=12:
#         ans="Child"
#     elif age<=19:
#         ans="Teenager" 
#     elif age<=65:
#         ans="Adult"
#     else:
#         ans="Senior"
# else:
#     ans="Invalid age!"      
# print(ans)


'''4.) Temperature Adviser: Write a program that suggests an activity based on the current temperature (in Celsius), following these guidelines:

Above 30°C: "It's hot. Let's go swimming!"
20°C to 30°C: "Perfect for a picnic."
10°C to 19°C: "Maybe wear a jacket?"
Below 10°C: "Too cold! Best to stay indoors."

The program takes the current temperature as input and prints the suggested activity.
Sample Input 1: 
15
Sample Output 1: 
Maybe wear a jacket?
Sample Input 2: 
8
Sample Output 2: 
Too cold! Best to stay indoors.
Sample Input 3: 
38
Sample Output 3: 
It's hot. Let's go swimming!
'''
# temperature=int(input("Enter the current temperature in Celsius: "))
# if temperature>30:
#     ans="It's hot. Let's go swimming!"
# elif temperature>=20:
#     ans="Perfect for a picnic."
# elif temperature>=10:
#     ans="Maybe wear a jacket?"
# else:
#     ans="Too cold! Best to stay indoors."
# print(ans)


'''5.) Maximum of Three Numbers: Write a program that takes three numbers as input and prints the largest number.

Sample Input 1: 
15 23 16
Sample Output 1: 
23
Sample Input 2: 
8 5 9
Sample Output 2: 
9
'''
# a,b,c=map(int,input("Enter three numbers(with space): ").split())
# if a>=b and a>=c:
#     largest=a
# elif b>=a and b>=c:
#     largest=b
# else:
#     largest=c
# print(largest)


'''6.) Sort Three Numbers: Write a program that takes three numbers as input and prints the numbers in ascending order (This program doesn't use an array).

Sample Input 1: 
15 23 16
Sample Output 1: 
15 16 23
Sample Input 2: 
8 5 9
Sample Output 2: 
5 8 9
'''
# a,b,c=map(int,input("Enter three numbers(with space): ").split())
# if a>b:
#     a,b=b,a
# if b>c:
#     b,c=c,b
# if a>b:
#     a,b=b,a
# print(a,b,c)