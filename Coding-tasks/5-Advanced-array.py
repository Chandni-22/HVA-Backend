'''1.) Longest Subarray with Increasing Numbers: You are given an integer array. Print the length of the longest subarray with increasing numbers.
A subarray is defined as a contiguous portion of an array.
Try not to use nested loop.
Sample Input: 
5 4 4 7 6 3 2 4 6 8 6 3 6 8 5
Sample Output: 
4
Explanation: The given array has many subarrays with increasing numbers. 
4 4 7 -> 5 4 4 7 6 3 2 4 6 8 6 3 6 8 5
2 4 6 8 -> 5 4 4 7 6 3 2 4 6 8 6 3 6 8 5
3 6 8 -> 5 4 4 7 6 3 2 4 6 8 6 3 6 8 5
Out of all these, the subarray with 4 increasing numbers is the longest.'''
# arr=list(map(int,input("Enter an array: ").split()))
# l=len(arr)
# i=0
# long=0
# count=1
# while i<(l-1):
#     if arr[i]>arr[i+1]:
#         if long<count:
#             long=count
#         count=1
#     else:
#         count+=1
#     i+=1
# print(long)


'''2.) Reverse an Array: You are given an array of integers. Create a new array with elements in reverse order. Print the new array.
Sample Input:
11 1 13 21 3 7
Sample Output:
7 3 21 13 1 11'''
# arr=list(map(int,input("Enter an array: ").split()))
# l=len(arr)
# i=0
# long=[]
# while i<l:
#     long+=[arr[i]]
#     i+=1
# print(long)


'''3.) Check Array for Palimdrome: You are given an array of integers. Check if the given array is a Palindrome. If it is a Palindrome array, print yes, else print no.
Note: A Palindrome Array is when the reverse of the array is the same as the original array.
Sample Input 1:
11 1 13 21 3 7
Sample Output 1:
No
Sample Input 2:
17 1 13 1 17
Sample Output 2:
Yes
Explanation 2: The reverse of the array reads same as the original array.'''
# arr=list(map(int,input("Enter an array: ").split()))
# l=len(arr)
# i=0
# while i<(l//2):
#     if arr[i]!=arr[(l-i)-1]:
#         print("No")
#         break
#     i+=1
# else:    
#     print("Yes")


'''4.) Maximum Frequency in an Array: You are given an array of integers. Find the element that appears the maximum number of times in an array. If multiple elements appear maximum number of times, you can print any.
Sample Input:
5 4 7 11 8 4 6 11 9
Sample Output:
4
Explanation: Both 4 and 11 appear 2 times. We can print any of 4 and 11, so we print 4.'''
# arr=list(map(int,input("Enter an array: ").split()))
# l=len(arr)
# i=0
# long=1
# count=1
# while i<l:
#     j=i+1
#     while j<(l):
#         if arr[j]==arr[i]:
#             count+=1
#         j+=1
#     if long<count:
#         long=count
#         a=arr[i]
#     count=1
#     i+=1
# print(a)


'''5.) Min and Max Difference in an Array: You are given an array of integers. Find the minimum and maximum difference between any two elements in an array.
Sample Input:
5 4 7 8 4 6 11 9
Sample Output:
0 7
Explanation: Minimum Difference: 4 - 4 = 0. Maximum Difference: 11 - 4 = 7'''
# arr=list(map(int,input("Enter an array: ").split()))
# l=len(arr)
# Min,Max=0,0
# i=0
# while i<l:
#     j=0
#     while j<l:
#         if i!=j:
#             diff=abs(arr[i]-arr[j])
#             if diff>Max:
#                 Max=diff
#             if diff<Min:
#                 Min=diff
#         j+=1
#     i+=1
# print(Min,Max)


'''6.) Sum of Array Except Self: You are given an array of integers. Print an array where each index has the sum of all numbers in the original array except the number at that index. 
Avoid using subtraction, and handle this with nested loops.
Sample Input:
7 3 6 7 5
Sample Output:
21 25 22 21 23
Explanation: The first element of the array is 7, so we print sum of all the elements except the number itself. 21 = 3 + 6 + 7 + 5.
The second element of the array is 3. 25 = 7 + 6 + 7 + 5.
The third element of the array is 6. 22 = 7 + 3 + 7 + 5.
The fourth element of the array is 7. 21 = 7 + 3 + 6 + 5.
The fifth element of the array is 5. 23 = 7 + 3 + 6 + 7.'''
# arr=list(map(int,input("Enter an array: ").split()))
# l=len(arr)
# a=[]
# i=0
# while i<l:
#     sum=0
#     j=0
#     while j<l:
#         if i!=j:
#             sum+=arr[j]
#         j+=1
#     a+=[sum]    
#     i+=1
# print(a)


'''7.) Frequency of Each Element in an Array: You are given an array of integers. Print the frequency of each element in the array.
Sample Input: 
3 6 2 1 7 3 7 4 1 7 4
Sample Output: 
3 2
6 1
2 1
1 2
7 3
4 2
Explanation: 3 appears twice, but we have to print its frequency only once. Same is with other numbers.'''
# arr=list(map(int,input("Enter an array: ").split()))
# l=len(arr)
# a=[]
# i=0
# while i<l:
#     count=1
#     j=0
#     while j<l:
#         if i!=j:
#             if arr[i]==arr[j]:
#                 count+=1
#         j+=1
#     o=0
#     while o<len(a):
#         if a[o]==arr[i]:
#             break
#         o+=1
#     else:
#         print(arr[i],count)
#         a+=[arr[i]]   
#     i+=1


'''8.) Sum of All Differences Between Pairs: You are given an array of integers. Calculate the sum of absolute differences between all pairs of numbers in the array.
Sample Input:
7 3 6 4
Sample Output:
14
Explanation: 
Absolute difference between 7 and 3 = 4
Absolute difference between 7 and 6 = 1
Absolute difference between 7 and 4 = 3
Absolute difference between 3 and 6 = 3
Absolute difference between 3 and 4 = 1
Absolute difference between 6 and 4 = 2
Sum of absolute differences between all pairs: 4+1+3+3+1+2 = 14'''
# arr=list(map(int,input("Enter an array: ").split()))
# l=len(arr)
# sum=0
# i=0
# while i<l:
#     j=i+1
#     while j<l:
#         sum+=abs(arr[i]-arr[j])
#         j+=1
#     i+=1
# print(sum)


'''9.) Find All Pairs with a Given Sum: You are given an integer array and a target sum. Find all pairs of elements in the array that add up to the given sum.
Sample Input: 
4 6 7 2 8 9 3 10
10
Sample Output: 
4 6
7 3
2 8
Explanation: The target sum here is 10. 10=4+6. 10=7+3. 10=2+8. Also, if you have printed the pair 4,6 once, you do not need to print it again as 6,4.'''
# arr=list(map(int,input("Enter an array: ").split()))
# t=int(input("Enter the target sum: "))
# l=len(arr)
# i=0
# while i<l:
#     j=i+1
#     while j<l:
#         if arr[i]+arr[j]==t:
#             print(arr[i],arr[j])
#         j+=1
#     i+=1


'''10.) First Repeat in an Array: You are given an integer array. Print the first number that repeats itself. If no number repeats in the array, print No. 
Sample Input 1:
5 11 4 7 8 4 6 11 7
Sample Output 1:
11
Explanation 1: In the given array, 11 is the first number that repeats itself.
Sample Input 2:
11 1 13 21 3 7
Sample Output 2:
No
Explanation 2: The given array doesn't contain any duplicate element, hence we print No.'''
# arr=list(map(int,input("Enter an array: ").split()))
# l=len(arr)
# i=0
# a=0
# while i<l:
#     j=i+1
#     while j<l:
#         if arr[i]==arr[j]:
#             a=arr[i]
#             break
#         j+=1
#     if  a:
#         print(a)
#         break   
#     i+=1
# if not(a):
#     print("No")


'''11.) Subarray with a Given Sum: You are given an integer array and a target sum. Print a subarray that adds up to the target sum.
If there are multiple possible subarrays, print the one that appears first and is smallest. And if, no such subarray is possible, print "Not Possible".
A subarray is defined as a contiguous portion of an array.
Sample Input 1: 
3 6 2 1 7
10
Sample Output 1: 
2 1 7
Explanation 1: 10 = 2+1+7. [2, 1, 7] is a subarray within the given array that adds up to 10.
Sample Input 2: 
3 6 2 1 7
14
Sample Output 2: 
Not Possible
Explanation 2: No subarray within the given array adds up to 14.'''
# arr=list(map(int,input("Enter an array: ").split()))
# t=int(input("Enter the target sum: "))
# l=len(arr)
# Min=[]
# i=0
# while i<l:
#     j=i+1
#     while j<=l:
#         if sum((arr[i:j]))==t and Min>(arr[i:j]):
#             Min=(arr[i:j])
#         j+=1
#     i+=1
# ans=Min if Min else "Not Possible"
# print(ans)


'''12.) Check for a Subarray in an Array: You are given two arrays. Check if the second array is a subarray of the first array. Print yes if it is, else print no.
A subarray is defined as a contiguous portion of an array.
Sample Input 1: 
3 6 2 1 7 6 4 9 7
7 6 4 9 7
Sample Output 1: 
Yes
Sample Input 2: 
3 6 2 1 7 6 4 9 7
7 6 4 9 6
Sample Output 2: 
No'''
# arr1=list(map(int,input("Enter an array: ").split()))
# arr2=list(map(int,input("Enter an array: ").split()))
# lent1=len(arr1)
# lent2=len(arr2)
# i=0
# while i<=(lent1-lent2):
#     j=0
#     while j<lent2:
#         if arr1[i+j]!=arr2[j]:
#             break
#         j+=1        
#     if j==lent2:
#         print("Yes")
#         break    
#     i+=1
# if i>lent1-lent2:
#     print("No")


'''13.) Common Elements in Two Arrays: You are given an integer n and two integer arrays each of length n. Print all the common elements between these two arrays.
Print the elements in an order as they appear in the first array. If one common element is repeated multiple times, print it just once. If there are no common elements, print No.
Sample Input 1: 
7
4 9 2 5 7 4 3
9 6 4 8 6 1 12
Sample Output 1: 
4 9
Explanation 1: In the given arrays, 4 is repeating multiple times, but you need to print it just once. Also, the order of printing 4 and 9 are as per their appearance in the 1st array.
Sample Input 2: 
7
2 7 6 4 7 4 3
8 5 9 1 5 8 9
Sample Output 2: 
No
Explanation 2: No elements are common in the two given array.'''
# n=int(input("Entera number: "))
# arr1=list(map(int,input("Enter an array: ").split()))
# arr2=list(map(int,input("Enter an array: ").split()))
# a=[]
# i=0
# while i<n:
#     count=1
#     j=0
#     while j<n:
#         if arr1[i]==arr2[j]:
#             l=arr1[i]
#             o=0
#             while o<len(a):
#                 if a[o]==l:
#                     break
#                 o+=1
#             else:
#                 a+=[l]
#                 break
#         j+=1      
#     i+=1
# if a:
#     print(*a)
# else:
#     print("No")


'''14.)Find all Subarrays of an Array: You are given an integer array. Print all the subarrays.
A subarray is defined as a contiguous portion of an array.
Print the subarrays in an order specified in the sample input / output.
Sample Input: 
3 2 1
Sample Output: 
3
3 2
3 2 1
2
2 1
1'''
# arr=list(map(int,input("Enter an array: ").split()))
# l=len(arr)
# i=0
# while i<l:
#     j=i+1
#     while j<=l:
#         print(arr[i:j])
#         j+=1
#     i+=1


'''15.) Sum of Subarrays: You are given an integer array. Print the sum of all possible subarrays.
A subarray is defined as a contiguous portion of an array.
Sample Input: 
3 7 5
Sample Output: 
52
Explanation: All the subarrays are:
3
3,7
3,7,5
7
7,5
5
Sum = 3 + (3+7) + (3+7+5) + 7 + (7+5) + 5 = 52'''
# arr=list(map(int,input("Enter an array: ").split()))
# l=len(arr)
# sum=0
# i=0
# while i<l:
#     a=0
#     j=i
#     while j<l:
#         a+=arr[j]
#         sum+=a
#         j+=1
#     i+=1
# print(sum)