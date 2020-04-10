""" 
Given an unsorted array arr[0..n-1] of size n, find the minimum length subarray arr[s..e] such that sorting this subarray makes the whole array sorted.
 """
""" 
If the input array is [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60], your program should be able to find that the subarray lies between the indexes 3 and 8.
"""



""" 
1) Znalezc pierwszy element z lewa na prawo ktorego next jest mniejszy niz on sam ->s
2) Znalezc pierwzy elemetnt od konca ktorego next jest wiekszy niz on sam ->e
3) Sprawdzic czy bedzie dzialalo (find max and min in there and check if passes)
4) If not:
    1) W arr[0,e] znalezc pierwszy element wiekszy niz min(arr[s,e])
    2) W arr[s,len(arr)] znalezc pierwszy element mniejszy od max(arr[s,e])
    3) Zmienic przedzial na te dwa elementy (Przedzial z tymi dwoma elementami jako końcami)
 """
