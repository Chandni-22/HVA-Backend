'''1.) Fibonacci Series: Write a program that takes a number n as input and prints the first n terms of the Fibonacci Series.
The Fibonacci Series is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
Series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …
Sample Input: 
10
Sample Output: 
0 1 1 2 3 5 8 13 21 34'''
# n=int(input("Enter number: "))
# a,b=0,1
# i=0
# while i<n:
#     print(a,end=" ")
#     a,b=b,a+b
#     i+=1


'''2.) Reverse a Number: Write a program that takes a number n as input and prints the reverse of the given number.
Sample Input: 
1132
Sample Output: 
2311
Explanation: The reverse of 1132 is 2311.'''
# n=int(input("Enter number: "))
# a=""
# while n>0:
#     a+=str(n%10)
#     n=n//10
# print(int(a))


'''3.) GCD (Greatest Common Divisor) or HCF (Highest Common Factor): You are given two positive integers a and b. Print the GCD or HCF of these two numbers.
Sample Input: 
20 16
Sample Output: 
4'''
# a,b=map(int,input("Enter numbers: ").split())
# while b>0:
#     a,b=b,a%b
# print(a)


'''4.) LCM (Least Common Multiple): You are given two positive integers a and b. Print the LCM of these two numbers.
Sample Input: 
20 16
Sample Output: 
80'''
# num1,num2=map(int,input("Enter numbers: ").split())
# a,b=num1,num2
# while b>0:
#     a,b=b,a%b
# HCF=a
# LCM=(num1*num2)//HCF
# print(LCM)