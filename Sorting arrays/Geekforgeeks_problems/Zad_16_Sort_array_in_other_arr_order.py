""" 
Given two arrays A1[] and A2[], sort A1 in such a way that the relative order among the elements will be same as those are in A2. For the elements not present in A2, append them at last in sorted order.
 """

""" 
1. Naive: connect the elements from 2-nd array to indexes in first and check if the element is present in 2-nd arr and put it on the index present there
 
2.  Zrobic struct el,count i przerobic tab2 na ten sposob
    Dalej binary searchem szukac elementu w tab2, jak jest tam to dodawac do countera, jak nie ma, to append to tab_to_ret


 """
class ar_s():
    def __init__(self,value=0):
        self.value=value
        self.count=0
        self.index_in_sorted=0
def Binary_Search(tab,el_searching,start=0,end=-1):
    """ 
    Returning -1 if there is no such an element,
    and if there is than returning el_index
     """
    if end==-1: end=len(tab)
    if start>=end : return -1
    mid=(start+end)//2
    if tab[mid]==el_searching:return mid
    if mid==0: return -1
    elif tab[mid]>el_searching: return Binary_Search(tab,el_searching,start,mid)
    elif tab[mid]<el_searching: return Binary_Search(tab,el_searching,mid+1,end)

def Build_My_tab(tab):
    tmp=[None]*len(tab)
    for i in range(len(tab)):
        tmp[i]=ar_s()
        tmp[i].value=tab[i]
        tmp[i].count=0
        tmp[i].index_in_sorted=-1
    return tmp

def zad(tab_1,tab_2):
    tab=Build_My_tab(tab_2)
    tab_1=sorted(tab_1)
    for i in range(len(tab_2)):
        while 1:
            k=Binary_Search(tab_1,tab_2[i])
            if k!=-1:
                tab[i].count+=1
                print(tab_1)
                del tab_1[k]
            else:
                break
    tab_to_ret=[]
    for i in range(len(tab)):
        while tab[i].count!=0:
          tab_to_ret.append(tab[i].value)
          tab[i].count-=1
    tab_to_ret=tab_to_ret+tab_1

    return tab_to_ret

print(zad([2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8],[2, 1, 8, 3]))







