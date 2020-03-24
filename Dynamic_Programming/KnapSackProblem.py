#Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

def NaiveRecursive(wagi,koszty,i,w):
    if i<0 or w<0:return 0
    if i==0:
        if w<wagi[0]:return 0
        if w>=wagi[0]:return koszty[0]
    return max(NaiveRecursive(wagi,koszty,i-1,w),NaiveRecursive(wagi,koszty,i-1,w-wagi[i]+koszty[i]))

print(NaiveRecursive([1,3,5,3,10,6],[5,2,4,1,7,5],5,10))