"""
Given two arrays: arr1[0..m-1] and arr2[0..n-1]. Find whether arr2[] is a subset of arr1[] or not. Both the arrays are not in sorted order. It may be assumed that elements in both array are distinct. 
"""

""" 
Input: arr1[] = {11, 1, 13, 21, 3, 7}, arr2[] = {11, 3, 7, 1}
Output: arr2[] is a subset of arr1[]

 """


""" 
Algorytm rozwiązania:

1. Posortować obydwa i szukac binary searchiem w pierwszym elementy z drugiego
2. Posortować obydwa i zrobić merge w taki sposób:
 while i < n and j < m: 
        if arr1[j] < arr2[i]: 
            j += 1
        elif arr1[j] == arr2[i]: 
            j += 1
            i += 1
        elif arr1[j] > arr2[i]: 
            return 0
    return False if i < n else True
O(mLogm + nLogn) - złożoność algorytmu
3. Hashing

 """