""" 
Inversion Count for an array indicates – how far (or close) the array is from being sorted. If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum.
Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j
 """

""" 
Input: arr[] = {8, 4, 2, 1}
Output: 6

Explanation: Given array has six inversions:
(8,4), (4,2),(8,2), (8,1), (4,1), (2,1).
"""

""" 
1. Naive solution - Znalezc inversji kazego z elementow tablicy - O(n^2)
2. O(nlogn) solution - to use Merge Sort
    Modify the function merge with the following tips:
    A = [1,3,5,7]     B = [2,4,6,8]
    For each step of merge, if A[i]>B[j] then:
        a) count_inv+=(mid-i+1), because all elements from A with index >i would have inversion with B[j] and adding 1 because Merge sorts takes middle into arr A and we need to include this element itself
        

 """