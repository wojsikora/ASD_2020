""" 
Given an unsorted array of integers, sort the array into a wave like array.An array 
‘arr[0..n-1]' is sorted in wave form if arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= …..
 """

""" 
Input:  arr[] = {10, 5, 6, 3, 2, 20, 100, 80}
 Output: arr[] = {10, 5, 6, 2, 20, 3, 100, 80} OR
                 {20, 5, 10, 2, 80, 6, 100, 3} OR
                 any other array that is in wave form
                  """

""" 
1. Naive
    Sort the array normaly and then rebuild it by taking elements from beg and end making new wave arr O(nlogn)
2. This can be done in O(n) time by doing a single traversal of given array. The idea is based on the fact that if we make sure that all even positioned (at index 0, 2, 4, ..) elements are greater than their adjacent odd elements, we don’t need to worry about odd positioned element. Following are simple steps.
1) Traverse all even positioned elements of input array, and do following.
….a) If current element is smaller than previous odd element, swap previous and current.
….b) If current element is smaller than next odd element, swap next and current.

 """


#First solution implementation

def zad(tab):
    tab=sorted(tab)
    tmp_tab=[0]*len(tab)
    curr_first=0
    curr_last=len(tab)-1
    _jedynka=False
    for i in range(len(tab)):
        if curr_first>curr_last: 
            print("Blad")
            break
        if _jedynka:
            tmp_tab[i]=tab[curr_first]
            curr_first+=1
            _jedynka=False
        else:
            tmp_tab[i]=tab[curr_last]
            curr_last-=1
            _jedynka=True
    return tmp_tab


# Python function to sort the array arr[0..n-1] in wave form, 
# i.e., arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= arr[5] 
def sortInWave(arr, n): 
	
	# Traverse all even elements 
	for i in range(0, n, 2): 
		
		# If current even element is smaller than previous 
		if (i> 0 and arr[i] < arr[i-1]): 
			arr[i],arr[i-1] = arr[i-1],arr[i] 
		
		# If current even element is smaller than next 
		if (i < n-1 and arr[i] < arr[i+1]): 
			arr[i],arr[i+1] = arr[i+1],arr[i] 

# Driver program 
arr = [10, 90, 49, 2, 1, 5, 23] 
sortInWave(arr, len(arr)) 
for i in range(0,len(arr)): 
	print arr[i], 
	
# This code is contributed by __Devesh Agrawal__ 


print(zad([20, 10, 8, 6, 4, 2]))


