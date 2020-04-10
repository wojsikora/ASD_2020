""" 
Given an array A[] consisting 0s, 1s and 2s. The task is to write a function that sorts the given array. The functions should put all 0s first, then all 1s and all 2s in last.
 """

""" 
1. Divide the array into 4 parts: for 0, for 1, for 2 and mixed, then going throught the mixed part add 0/1/2 to the matching ones using some ints to remeber pace
2. Count the number of 0/1/2s in the array and then return iterating through the tab 
  """
  