# Given an array of integers, find the first recurring number
# Ex, the array is: [1, 2, 3, 56, 12, 6, 7, 1, 2]
# The answer is 2.

# O(n^2) Approach:
testArr = [1, 2, 3, 56, 12, 6, 7, 1, 9]
#for i in range(len(testArr)):
#    for j in range(i + 1, len(testArr)):
#        if testArr[i] == testArr[j]:
#            print(testArr[i])

# O(n) Approach:
hashMap = {}
for i, number in enumerate(testArr):
    if number in hashMap:
        print(number)
        break
    else:
        hashMap[i] = number
        
    