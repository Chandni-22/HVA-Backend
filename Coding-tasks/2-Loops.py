'''1.) N times "Hello World": You are given an integer n. Print "Hello World" n times.
Sample Input: 
5
Sample Output: 
Hello World
Hello World
Hello World
Hello World
Hello World'''
# n=int(input("Enter a number: "))
# i=1
# while i<=n:
#     print("Hello World")
#     i+=1


'''2.) N times * in same line: You are given an integer n. Print * n times in the same line with space in between.
Sample Input: 
5
Sample Output: 
* * * * * '''
# n=int(input("Enter a number: "))
# i=1
# while i<=n:
#     print("*",end=" ")
#     i+=1


'''3.) First n Natural Numbers: You are given an integer n. Print the first n natural numbers.
Sample Input: 
7
Sample Output: 
1 2 3 4 5 6 7'''
# n=int(input("Enter a number: "))
# i=1
# while i<=n:
#     print(i,end=" ")
#     i+=1


'''4.) All Even Numbers till n: You are given an integer n. Print all the even numbers less than equal to n.
Sample Input: 
14
Sample Output: 
2 4 6 8 10 12 14'''
# n=int(input("Enter a number: "))
# i=2
# while i<=n:
#     print(i,end=" ")
#     i+=2


'''5.) All Square Numbers till n: You are given an integer n. Print all the square numbers less than equal to n.
Sample Input: 
50
Sample Output: 
1 4 9 16 25 36 49'''
# n=int(input("Enter a number: "))
# i=1
# while i<=n:
#     a=i**2
#     if a<=n:
#         print(a,end=" ")
#     i+=1


'''6.) First n Even Numbers: You are given an integer n. Print the first n even numbers.
Sample Input: 
7
Sample Output: 
2 4 6 8 10 12 14'''
# n=int(input("Enter a number: "))
# count,i=0,1
# while count<n:
#     if i%2==0:
#         print(i,end=" ")
#         count+=1
#     i+=1


'''7.) First n Odd Numbers: You are given an integer n. Print the first n odd numbers.
Sample Input: 
7
Sample Output: 
1 3 5 7 9 11 13'''
# n=int(input("Enter a number: "))
# count,i=0,1
# while count<n:
#     if i%2!=0:
#         print(i,end=" ")
#         count+=1
#     i+=1


'''8.) First n Square Numbers: You are given an integer n. Print the first n square numbers.
Sample Input: 
7
Sample Output: 
1 4 9 16 25 36 49'''
# n=int(input("Enter a number: "))
# i=1
# while i<=n:
#     print(i**2,end=" ")
#     i+=1


'''9.) Multiplication Table of n: You are given an integer n. Print the multiplication table of n till count 10.
Sample Input: 
7
Sample Output: 
7 14 21 28 35 42 49 56 63 70
Explanation: Print 7*1, 7*2, …, 7*10.'''
# n=int(input("Enter a number: "))
# i=1
# while i<=10:
#     print(i*n,end=" ")
#     i+=1


'''10.) Factors of a Number: Write a program that takes a number n as input and prints all the factors of the number.
Sample Input: 
24
Sample Output: 
1 2 3 4 6 8 12 24
Explanation: The factors of 24 are 1, 2, 3, 4, 6, 8, 12, 24.'''
# n=int(input("Enter a number: "))
# i=1
# while i<=(n//2):
#     if n%i==0:
#         print(i,end=" ")
#     i+=1
# print(n)


'''11.) Series: 3, 5, 7, 9, 11, …: You are given an integer n. Print first n terms of the series 3, 5, 7, 9, 11…
Sample Input: 
7
Sample Output: 
3 5 7 9 11 13 15
Explanation: The series starts with 3 and every time adds 2 to get the next term.'''
# n=int(input("Enter a number: "))
# i,count=1,0
# while count<n:
#     i+=2
#     print(i,end=" ")
#     count+=1


'''12.) Series: 2, 5, 8, 11, 14, …: You are given an integer n. Print first n terms of the series 2, 5, 8, 11, 14…
Sample Input: 
7
Sample Output: 
2 5 8 11 14 17 20
Explanation: The series starts with 2 and every time adds 3 to get the next term.'''
# n=int(input("Enter a number: "))
# i,count=2,0
# while count<n:
#     print(i,end=" ")
#     count+=1
#     i+=3


'''13.) Series: 3, 6, 12, 24, 48, …: You are given an integer n. Print first n terms of the series 3, 6, 12, 24, 48…
Sample Input: 
7
Sample Output: 
3 6 12 24 48 96 192
Explanation: The series starts with 3 and every time multiplies 2 to get the next term.'''
# n=int(input("Enter a number: "))
# i,count=3,0
# while count<n:
#     print(i,end=" ")
#     count+=1
#     i*=2


'''14.) Sum of First n Natural Numbers: You are given an integer n. Print the sum of the first n Natural Numbers.
Note: Use a loop instead of a mathematical formula.
Sample Input: 
7
Sample Output: 
28
Explanation: Sum of 1+2+3+4+5+6+7 = 28'''
# n=int(input("Enter a number: "))
# i,sum=1,0
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)


'''15.) Sum of Series: 3, 5, 7, 9, 11, …: You are given an integer n. Print the sum of the first n terms of the series 3, 5, 7, 9, 11….
Note: Use a loop instead of a mathematical formula.
Sample Input: 
7
Sample Output: 
63
Explanation: Sum of 3+5+7+9+11+13+15 = 63'''
# n=int(input("Enter a number: "))
# i,count,sum=3,0,0
# while count<n:
#     print(i)
#     sum+=i
#     count+=1
#     i+=2
# print(sum)


'''16.) Factorial of a Number: Write a program to calculate the factorial of a given number n. 
The factorial of a number n is the product of all positive integers less than or equal to n.
Sample Input: 
6
Sample Output: 
720
Explanation: 720 = 6*5*4*3*2*1'''
# n=int(input("Enter a number: "))
# i,factorial=1,1
# while i<=n:
#     factorial*=i
#     i+=1
# print(factorial)


'''17.) Counting Digits in a Number: Write a program that takes a number n as input and prints the number of digits the number has.
Sample Input: 
1132
Sample Output: 
4'''
# n=int(input("Enter a number: "))
# count=0
# while n>0:
#     n=n//10
#     count+=1
# print(count)

'''18.) Sum of Digits of a Number: Write a program that calculates the sum of all the digits in a given number n.
Sample Input: 
1132
Sample Output: 
7
Explanation: 7 = 1+1+3+2'''
# n=int(input("Enter a number: "))
# sum=0
# while n>0:
#     sum+=n%10
#     n=n//10
# print(sum)