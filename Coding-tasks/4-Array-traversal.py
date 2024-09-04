'''1.) Square - Each Array Element: You are given an integer array. Traverse through the array and print the square for each element.
Sample Input:
5 3 4 7 2 9
Sample Output:
25 9 16 49 4 81'''
# arr=list(map(int,input("Enter an array: ").split()))
# i=0
# while i<(len(arr)):
#     print((arr[i])**2,end=" ")
#     i+=1


'''2.) Odd or Even - Each Array Element: You are given an integer array. Traverse through the array and for each element, if the element is odd print "Odd", else print "Even".
Sample Input:
4 7 9 10 13 17
Sample Output: 
Even
Odd
Odd
Even
Odd
Odd'''
# arr=list(map(int,input("Enter an array: ").split()))
# i=0
# while i<(len(arr)):
#     if (arr[i])%2==0:
#         print("Even")
#     else:
#         print("Odd")
#     i+=1


'''3.) Odd Count in an Array: You are given an integer array. Print the number of odd numbers in the array.
Sample Input:
4 7 9 10 13 17
Sample Output: 
4 
Explanation: There are 4 odd numbers in the given numbers: 7, 9, 13, 17.'''
# arr=list(map(int,input("Enter an array: ").split()))
# i=0
# count=0
# while i<(len(arr)):
#     if (arr[i])%2!=0:
#         count+=1
#     i+=1
# print(count)


'''4.) Number Count in an Array: You are given an integer array. You are also given a number. Print the number of times the number appears in the array.
Sample Input:
4 7 9 10 7 14 12 4 7 27
7
Sample Output: 
3
Explanation: The given number 7 appears 3 times in the given array.'''
# arr=list(map(int,input("Enter an array: ").split()))
# n=int(input("Enter a number: "))
# i=0
# count=0
# while i<(len(arr)):
#     if (arr[i])==n:
#         count+=1
#     i+=1
# print(count)


'''5.) Sum of Elements in an Array: You are given an integer array. Add all the numbers present in the array and print the sum.
Sample Input: 
10 5 6 3 4 3 5 6
Sample Output: 
42
Explanation: 10+5+6+3+4+3+5+6 = 42'''
# arr=list(map(int,input("Enter an array: ").split()))
# i=0
# sum=0
# while i<(len(arr)):
#     sum+=arr[i]
#     i+=1
# print(sum)


'''6.) Average of Elements in an Array: You are given an integer array. Find the average of all the numbers present in the array.
Sample Input: 
10 5 6 3 4 3 5 6
Sample Output: 
5.25
Explanation: There are 8 elements in the given array. Sum = 10+5+6+3+4+3+5+6 = 42. Average = 42/8 = 5.25'''
# arr=list(map(int,input("Enter an array: ").split()))
# l=len(arr)
# i=0
# sum=0
# while i<l:
#     sum+=arr[i]
#     i+=1
# print(sum/l)


'''7.) Product of Elements in an Array: You are given an integer array. Multiply all the numbers present in the array and print the final product.
Sample Input: 
3 2 5 1 4
Sample Output: 
120
Explanation: 3*2*5*1*4 = 120'''
# arr=list(map(int,input("Enter an array: ").split()))
# l=len(arr)
# i=0
# product=1
# while i<l:
#     product*=arr[i]
#     i+=1
# print(product)


'''8.) Minimum in an Array: You are given an integer array. Find the minimum element of the array.
Sample Input: 
10 5 6 3 4 3 5 6
Sample Output: 
3
Explanation: Here 3 is the minimum number. But since 3 is present more than once, we print the index of the first occurrence.'''
# arr=list(map(int,input("Enter an array: ").split()))
# l=len(arr)
# i=0
# Min=arr[0]
# index=0
# while i<l:
#     if Min>arr[i]:
#         Min=arr[i]
#         index=i    
#     i+=1
# print(index)


'''9.) Minimum Index in an Array: You are given an integer array. Find the index of the minimum element of the array. If there are multiple occurrences of the minimum number, print the index of the first occurrence of the minimum number. 
Note: The index will be calculated from 1.
Sample Input: 
10 5 6 3 4 3 5 6
Sample Output: 
4
Explanation: Here 3 is the minimum number. But since 3 is present more than once, we print the index of the first occurrence.'''
# arr=list(map(int,input("Enter an array: ").split()))
# l=len(arr)
# i=0
# Min=arr[0]
# index=0
# while i<l:
#     if Min>arr[i]:
#         Min=arr[i]
#         index=i    
#     i+=1
# print(index+1)


'''10.) Maximum Sum of Two Consecutive Elements: You are given an integer array. Print the maximum sum of two consecutive integers in the given array.
Sample Input: 
3 6 2 1 8 2 5 7 1
Sample Output: 
12
Explanation: 5+7 = 12 is the maximum sum of two consecutive integers in the given array.'''
# arr=list(map(int,input("Enter an array: ").split()))
# l=len(arr)
# i=0
# sum=0
# while i<(l-1):
#     if sum<(arr[i]+arr[i+1]):
#         sum=(arr[i]+arr[i+1])
#     i+=1
# print(sum)


'''11.) Count Elements until Negative: You are given an integer array. Count all the numbers present in the array till you encounter a negative number and print the count. If no negative number is present, count till the end.
Sample Input: 
10 5 6 3 -1 4 -3 5 6
Sample Output: 
4
Explanation: There are 4 elements before the first negative number appears.'''
# arr=list(map(int,input("Enter an array: ").split()))
# l=len(arr)
# i=0
# count=0
# while i<(l):
#     if arr[i]>=0:
#         count+=1
#     else:
#         break    
#     i+=1
# print(count)


'''12.) Sum until Zero: You are given an integer array. Add all the numbers present in the array till you encounter a 0 and print the sum. If no 0 is present, add till the end.
Sample Input: 
10 5 6 3 0 4 3 5 6
Sample Output: 
24
Explanation: 10+5+6+3 = 24'''
# arr=list(map(int,input("Enter an array: ").split()))
# l=len(arr)
# i=0
# sum=0
# while i<(l):
#     if arr[i]>0 or 0>arr[i]:
#         sum+=arr[i]
#     else:
#         break    
#     i+=1
# print(sum)


'''13.) Linear Search: You are given an integer array. Take another number as input and search if the number is present in the given array. If the number is present, print "Yes", else print "No".
Sample Input 1:
11 1 13 21 3 7
3
Sample Output 1:
Yes
Sample Input 2:
11 1 13 21 3 7
5
Sample Output 2:
No'''
# arr=list(map(int,input("Enter an array: ").split()))
# n=int(input("Enter a number: "))
# l=len(arr)
# i=0
# while i<(l):
#     if arr[i]==n:
#         print("Yes")
#         break  
#     i+=1
# else:
#     print("No")


'''14.) Check Array for Negative Numbers: You are given an array of integers. Check if the array has any negative numbers. If the array has any negative number, print yes. Else, print no.
Sample Input 1:
11 1 13 21 3 7
Sample Output 1:
No
Explanation 1: The given array has no negative number. 
Sample Input 2:
6 8 9 -1 14 8 -3 6
Sample Output 2:
Yes
Explanation 2: The given array has negative numbers, -1 and -3.'''
# arr=list(map(int,input("Enter an array: ").split()))
# l=len(arr)
# i=0
# while i<(l):
#     if arr[i]<0:
#         print("Yes")
#         break  
#     i+=1
# else:
#     print("No")


'''15.) Check Array for Ascending Order: You are given an array of integers. Check if the array is in Ascending Order. If yes, print "Yes", else print "No.
Sample Input 1:
3 5 10 13 16 12 14
Sample Output 1:
No
Explanation 1: The given array is not in ascending order.
Sample Input 2:
3 5 10 13 16 25 33
Sample Output 2:
Yes
Explanation 2: The given array is in ascending order.'''
# arr=list(map(int,input("Enter an array: ").split()))
# l=len(arr)
# i=0
# while i<(l-1):
#     if arr[i]>arr[i+1]:
#         print("No")
#         break  
#     i+=1
# else:
#     print("Yes")


'''16.) First Perfect Square: You are given an array of integers. Print the first element of the array that is a perfect square. If there are no perfect squares, print No.
Sample Input 1:
3 6 7 4 6 9 1 23
Sample Output 1:
4
Explanation 1: In the given array, the first perfect square to appear is 4.
Sample Input 2:
10 8 14 11 6 15
Sample Output 2:
No
Explanation 2: In the given array, there are no perfect squares.'''
# arr=list(map(int,input("Enter an array: ").split()))
# l=len(arr)
# i=0
# while i<(l):
#     a=arr[i]**0.5
#     if a==int(a):
#         print(arr[i])
#         break
#     i+=1
# else:
#     print("No")


'''17.) First Element Greater Than K: You are given an array of integers and another integer K. Print the first element of the array that is greater than K. If there are no elements greater than K, print No.
Sample Input 1:
3 5 10 25 16 12 14
11
Sample Output 1:
25
Explanation 1: In the given array, the first element greater than 11 is 25.
Sample Input 2:
3 5 10 13 16 12 14
19
Sample Output 2:
No
Explanation 2: In the given array, there are no elements greater than 19.'''
# arr=list(map(int,input("Enter an array: ").split()))
# k=int(input("Enter a number: "))
# l=len(arr)
# i=0
# while i<(l):
#     if arr[i]>k:
#         print(arr[i])
#         break  
#     i+=1
# else:
#     print("No")