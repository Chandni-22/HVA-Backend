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

'''One way:'''
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

'''Second way:'''
# for _ in range(int(input())):
#     s=input()
#     ans="YES" if s==s[::-1] else "NO" 
#     print(ans)


'''Problem 2.): Search Insert Position: Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
'''
# nums=list(map(int,input().split()))
# target=int(input())

# if target in nums:
#     print(nums.index(target))
# else:
#     count=0
#     i=0
#     while i<(len(nums)):
#         if target<nums[i]:
#             a=i
#             count+=1
#             break
#         i+=1
#     if count>0:
#         print(a)
#     else:
#         print(len(nums)) 


'''Problem 2.): Two Sum: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''
# nums=list(map(int,input().split()))
# target=int(input())

# a=[]
# i=0
# while i<(len(nums)-1):
#     j=i+1
#     while j<(len(nums)):
#         if (nums[i]+nums[j])==target:
#             a.append(i)
#             a.append(j)
#             break
#         j+=1
#     if a:
#         break
#     else:
#         i+=1
# print(a)