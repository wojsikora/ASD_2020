def merge(l,r):
    # O(n)
    i_l=0
    i_r=0
    tab=[]
    while i_l<len(l) and i_r<len(r):
        if l[i_l]<r[i_r]:
            tab.append(l[i_l])
            i_l+=1
        else:
            tab.append(r[i_r])
            i_r+=1
    while i_l<len(l) and i_r>=len(r):
        tab.append(l[i_l])
        i_l+=1
    while i_l>=len(l) and i_r<len(r):
        tab.append(r[i_r])
        i_r+=1
    return tab
#Wersja pythonowska Merge_sorta
def Merge_sort(tab):
    if len(tab)==1:
        return tab
    if len(tab)>1:
        med=len(tab)//2
        return merge(Merge_sort(tab[:med]),Merge_sort(tab[med:]))

print(Merge_sort([4,2,1,0,0,0,5]))

