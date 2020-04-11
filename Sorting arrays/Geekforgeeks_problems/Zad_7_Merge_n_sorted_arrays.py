""" 
Given N machines. Each machine contains some numbers in sorted form. But the amount of numbers, each machine has is not fixed. Output the numbers from all the machine in sorted non-decreasing form.
Representation of stream of numbers on each machine is considered as linked list.
 """

""" 

Machine M1 contains 3 numbers: {30, 40, 50}
       Machine M2 contains 2 numbers: {35, 45} 
       Machine M3 contains 5 numbers: {10, 60, 70, 80, 100}
       Output: {10, 30, 35, 40, 45, 50, 60, 70, 80, 100}
 """

""" 
1) Zrobic min heapa z pierwszych(zerowych) elementów kazdego z arrays
2) Zdejmować min i zamieniac go na min_el->next dopoki będą elementy w kopcu
"""
#Implementacja DOESN'T WORK







