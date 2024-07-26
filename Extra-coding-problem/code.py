'''Problem 1.): Bob's Bizarre Binary Bakery
Problem Statement: Bob owns a bakery where he makes binary cakes. Each cake is decorated with a binary number (a string consisting of 0s and 1s). One day, Bob's mischievous cat, Whiskers, jumped onto the counter and scrambled the binary decorations on the cakes. Bob needs to quickly determine if each cake's binary number is a palindrome (reads the same backward as forward) to impress his customers and keep his bakery's reputation intact.
Help Bob by writing a program to determine if each binary string is a palindrome.
Instructions:
1.) Read the integer t representing the number of cakes.
2.) For each binary string, determine if it is a palindrome.
3.) Output "YES" or "NO" for each binary string.
Input:
3
101
1001
110
Output:
YES
YES
NO
Explanation:
- "101" is the same backward as forward.
- "1001" is the same backward as forward.
- "110" is not the same backward as forward.'''

# t=int(input())
# i=1
# while i<=t:
#     s=input()
#     n=int(s)
#     revs=""
#     while n>0:
#         a=n%10
#         revs+=str(a)
#         n=n//10
#     if revs==s:
#         print("YES")
#     else:
#         print("NO")


for _ in range(int(input())):
    s=input()
    ans="YES" if s==s[::-1] else "NO" 
    print(ans)