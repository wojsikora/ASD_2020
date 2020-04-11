""" 
Given an unsorted array, sort the given array. You are allowed to do only following operation on array.
flip(arr, i): Reverse array from 0 to i 

Imagine a hypothetical machine where flip(i) always takes O(1) time. Write an efficient program for sorting a given array in O(nLogn) time on the given machine
 """

""" 
1. O(n^2)
    curr_arr_size=len(arr)-1
    1) Find Max element in arr
    2) do flip(arr,max_el_index)
    3) do flip(0,curr_arr_size)
    4) curr_arr_size--
    5) Do same for new max_el in arr[0,curr_arr_size] while curr_arr_size>=0

2. O(nlogn) 
    Algorytm polega na wstawianiu na poczatek min in curr_subarray

    1) Bierzemy i-ty element zeby go wsawic w arr[0,i-1]
    2) Szukamy binary searchem mu miejsce
    3) Wstawiamy na jego miejsce robiąc odpowiednio:
        Staramy sie nie zmieniajac nic w arr zamienic arr[0] i arr[i] zeby potem miec mozliwosc wstawiania w potrzebne miejsce
        0) DLA 20 w tym arr              {12, 15, 18, 30, 35, 40, 20, 6, 90, 80}
        1) Find j using ceilSearch (In the above example j is 3).
        2) flip(arr, j-1) (array becomes {18, 15, 12, 30, 35, 40, "20", 6, 90, 80})
        3) flip(arr, i-1); (array becomes {40, 35, 30, 12, 15, 18, "20", 6, 90, 80})
        4) flip(arr, i); (array becomes {"20", 18, 15, 12, 30, 35, 40, 6, 90, 80})
        5) flip(arr, j); (array becomes {12, 15, 18, "20", 30, 35, 40, 6, 90, 80})

 """