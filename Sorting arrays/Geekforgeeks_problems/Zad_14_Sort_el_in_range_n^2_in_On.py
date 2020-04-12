""" 
Given an array of numbers of size n. It is also given that the array elements are in range from 0 to n2 – 1. Sort the given array in linear time.
 """


""" 
Stosujemy sortowanie pozycyjne (radix sort), ale podstawą naszego systemu liczenia nie jest 10, tylko n. W związku z tym musimy wykonać dwa sortowania z użyciem sortowania przez zliczanie (counting sort), które wykona się w czasie O(n)


1.Let there be d digits in input integers. Radix Sort takes O(d*(n+b)) time where b is the base for representing numbers, for example, for decimal system, b is 10. Since n2-1 is the maximum possible value, the value of d would be O(logb(n)). So overall time complexity is O((n+b)*O(logb(n)). Which looks more than the time complexity of comparison based sorting algorithms for a large k. The idea is to change base b. If we set b as n, the value of O(logb(n)) becomes O(1) and overall time complexity becomes O(n). 
 
  """