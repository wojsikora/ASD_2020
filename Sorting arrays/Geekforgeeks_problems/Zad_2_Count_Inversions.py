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

def merge(tab,p,sr,k):
    # Uwaga, sr is included in left_tab
    counter=0
    i=p
    j=sr+1
    tab_to_ret = [0] * (k-p+1)
    curr_index=0
    while i<=sr and j<=k:
        if tab[i]<=tab[j]:
            tab_to_ret[curr_index] = tab[i]
            curr_index+=1
            i+=1
        else:
            counter+=(sr-i+1)
            tab_to_ret[curr_index] = tab[j]
            curr_index+=1
            j+=1
    while i>sr and j<=k:
        tab_to_ret[curr_index] = tab[j]
        curr_index+=1
        j+=1
    while i<=sr and j>k:
        tab_to_ret[curr_index] = tab[i]
        curr_index+=1
        i+=1
    return tab_to_ret,counter
counter=0
def merge_sort(tab,p,k):
    global counter
    if p!=k:
        sr=(p+k)//2
        merge_sort(tab,p,sr)
        merge_sort(tab,sr+1,k)
        tab,counter_tmp = merge(tab,p,sr,k)
        counter+=counter_tmp
    return tab

def zad_2(tab):
    merge_sort(tab,0,len(tab)-1)
    print(counter)

zad_2([3, 1, 2])

