""" 
Given a sorted array and a number x, find a pair in array whose sum is closest to x.
 """
""" 
Input: arr[] = {10, 22, 28, 29, 30, 40}, x = 54
Output: 22 and 30
 """




""" 
1.  O(n)
    1) Algorytm polega na 2 markerach z obu stron
    2) Iterowanie po tablice i szukanie min(poprz_rozn,curr_roznica)
    3) Zwracanie current roznicy


 """

def zad(tab,sum):
    diff=float('+inf')
    first=0
    last=len(tab)-1
    first_in_pair=-1
    second_in_pair=-1
    while first<last:
        if tab[first]+tab[last]==sum:
            return 0
        if tab[first]+tab[last]<sum:
            if diff>min(diff,abs(sum-(tab[first]+tab[last]))):
                diff=min(diff,abs(sum-(tab[first]+tab[last])))
                first_in_pair=tab[first]
                second_in_pair=tab[last]

            first+=1
        if tab[first]+tab[last]>sum:
            if diff>min(diff,abs(sum-(tab[first]+tab[last]))):
                diff=min(diff,abs(sum-(tab[first]+tab[last])))
                first_in_pair=tab[first]
                second_in_pair=tab[last]
            last-=1
    return first_in_pair,second_in_pair
print(zad([10, 22, 28, 29, 30, 40],54))