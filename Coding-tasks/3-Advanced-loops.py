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


'''5.) Binary to Decimal: Write a program that takes a Binary Number B as input and prints the Decimal equivalent of the given input.
Sample Input: 
1000
Sample Output: 
8'''
# binary=int(input("Enter binary number: "))
# decimal=0
# i=0
# while binary>0:
#     decimal+=(binary%10)*(2**i)
#     i+=1
#     binary=binary//10
# print(decimal)


'''6.) Decimal to Binary: Write a program that takes a Decimal Number D as input and prints the Binary equivalent of the given input.
Sample Input: 
8
Sample Output: 
1000'''
# decimal=int(input("Enter decimal number: "))
# binary=""
# while decimal>0:
#     binary+=str(decimal%2)
#     decimal=decimal//2
# binary=int(binary[::-1])
# print(binary)


'''7.) Is Prime?: You are given an integer n. Print yes, if it is a prime number. Print no, if it is not a prime number.
Sample Input 1: 
49
Sample Output 1: 
No
Sample Input 2: 
37
Sample Output 2: 
Yes'''
# n=int(input("Enter numbers: "))
# if (n<2) or (n>2 and n%2==0):
#     prime="No"
# elif n==2:
#     prime="Yes"
# else:
#     i=2
#     while i<=(n//2):
#         if n%i==0:
#             prime="No"
#             break
#         i+=1
#     else:
#         prime="Yes"    
# print(prime)


'''8.) Is Perfect Number?: You are given an integer n. Print yes, if it is a Perfect Number. Print no, if it is not a Perfect Number.
A Perfect Number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
Sample Input 1: 
28
Sample Output 1: 
Yes
Explanation 1: The factors of 28 are 1, 2, 4, 7, 14, 28. We don't consider the number itself. 28 = 1+2+4+7+14.
Sample Input 2: 
24
Sample Output 2: 
No
Explanation 2: The factors of 24 are 1, 2, 3, 4, 6, 8, 12, 24. We don't consider the number itself. But 24 != 1+2+3+4+6+8+12.'''
# n=int(input("Enter numbers: "))
# i=1
# sum=0
# while i<=(n//2):
#     if n%i==0:
#         sum+=i
#     i+=1
# ans= "Yes" if sum==n else "No"
# print(ans)


'''9.) Is Armstrong Number?: You are given an integer n. Print yes, if it is an Armstrong Number. Print no, if it is not an Armstrong Number.
An Armstrong Number is a positive number that equals the sum of its digits, each raised to the power of the number of digits.
Sample Input 1: 
1634
Sample Output 1: 
Yes
Explanation 1: 1634 has 4 digits, so we raise each digit to the power of 4. 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634 
Sample Input 2: 
153
Sample Output 2: 
Yes
Explanation 2: 153 has 3 digits, so we raise each digit to the power of 3. 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153'''
# n=int(input("Enter numbers: "))
# a=n
# l=len(str(n))
# sum=0
# while a>0:
#     sum+=(a%10)**l
#     a=a//10
# ans= "Yes" if sum==n else "No"
# print(ans)


'''10.) Star Pattern 1: Print the following pattern based on the given input.
Sample Input: 
6
Sample Output: 
*
**
***
****
*****
******
Explanation: Since the input is 6, it prints a total of 6 lines. In each line, the star count increases.'''
# n=int(input("Enter numbers: "))
# i=1
# while i<=n:
#     print("*"*i)
#     i+=1


'''11.) Star Pattern 2: Print the following pattern based on the given input.
Sample Input: 
6
Sample Output: 
     *
    **
   ***
  ****
 *****
******
Explanation: Since the input is 6, it prints a total of 6 lines. In each line, the star count increases and the leading space decreases.'''
# n=int(input("Enter numbers: "))
# i=1
# while i<=n:
#     print(" "*(n-i),end="")
#     print("*"*i)
#     i+=1


'''12.) Star Pattern 3:
Print the following pattern based on the given input.
Sample Input: 
6
Sample Output: 
*
 *
  *
   *
    *
     *
Explanation: Since the input is 6, it prints a total of 6 lines. In each line, it prints only one star, but the leading space increases.'''
# n=int(input("Enter numbers: "))
# i=0
# while i<n:
#     print(" "*i,end="")
#     print("*")
#     i+=1


'''13.) Star Pattern 4: Print the following pattern based on the given input.
Sample Input: 
5
Sample Output: 
    *
   ***
  *****
 *******
*********
Explanation: Since the input is 5, it prints a total of 5 lines of stars. Each line has stars as well as leading spaces. In each line, the star count increases by 2, but the leading space decreases by 1.'''
# n=int(input("Enter numbers: "))
# i=1
# while i<=n:
#     print(" "*(n-i)+"*"*((2*i)-1))
#     i+=1


'''14.) First n prime numbers: You are given an integer n. Print the first n prime numbers.
Sample Input: 
7
Sample Output: 
2 3 5 7 11 13 17'''
# n=int(input("Enter numbers: "))
# i=2
# count=0
# while count<n:
#     j=2
#     while j<=(i//2):
#         if i%j==0:
#             break
#         j+=1
#     else:
#         print(i,end=" ")
#         count+=1
#     i+=1