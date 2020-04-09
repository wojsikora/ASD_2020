""" 
Print the elements of an array in the decreasing frequency if 2 numbers have same frequency then print the one which came first.

Input:  arr[] = {2, 5, 2, 8, 5, 6, 8, 8}
Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6}
 """
 


""" 
1. n^3 naive solution
    1) Dla każdego elementa liczymy frequensy O(n^3)
    2) Sortuje po frequensy i wypisuje O(nlogn)

2.  nlogn solution
    1) O(nlogn) Sortowanie
    2) Zrobic tablice wag iterujac po pierwotnej O(n)
    3) Posortowac O(nlogn) używając sortowania stabilnego
"""

def sort_by_freq(tab):
    tab=sorted(tab)
    for j in range(len(tab)):
        tab[j]=[0,tab[j]]
    print(tab)
    c=1
    for i in range(len(tab)-1):
        """ if i+1==len(tab)-1:
            if c!=0:
                if tab[i][0]==tab[i+1][0]:
                     """
        if tab[i][1]==tab[i+1][1]:
            c+=1
        else:
            tab[i][0]=c
            c=1
    tab[len(tab)-1][0]=c
    tab=sorted(tab,reverse=True)
    while i<len(tab):
        if tab[i][0]==0:
            del tab[i]
        i+=1
    print(tab)

sort_by_freq([2, 5, 2, 8, 5, 6, 8, 8])

