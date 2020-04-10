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

# ZACZYNAMY OD 1!!
def parent(i):return i//2
def left(i): return i*2
def right(i): return i*2 + 1
def size(k): return k[0]
def heapify_min(tab,i):   
    
    L=left(i)
    R=right(i)
    min=i
    size=tab[0]
    if L<=size and tab[L].value<tab[min].value:
        min=L
    if R<=size and tab[R].value<tab[min].value:
        min=R
    if min!=i:
        tab[i],tab[min]=tab[min],tab[i]
        heapify_min(tab,min)
    return tab
def BuildHeap_min(tab):
    #Funckja dziala z dołu w górę! (Bo musisz naprawic calkiem kopiec, a naprawiajac z dzieci
    #nie robisz duzo razy to same)
    for i in range(tab[0]//2,0,-1):
        heapify_min(tab,i)
    return tab
 
class Node:
    def __init__(self = None,value = None):
        self.value=value
        self.next = None
        self.is_empty = value == None
        #self.state = None
    def _out(self):
        new_list=self
        tab = []
        while new_list!= None:
            tab.append(new_list.value)
            new_list=new_list.next
        print(tab)
    def _in(self,n):
        new_obj=Node()
        to_return = new_obj
        for _ in range(n-1):
            tmp=Node()
            new_obj.value=int (input())
            new_obj.next = tmp
            new_obj = tmp
        new_obj.value = int (input())
        new_obj.next=None
        return to_return
    def _len(self):
        tmp=self
        counter=0
        while tmp!= None:
            counter+=1
            tmp=tmp.next
        return int (counter)
    def _add_to_end(self,val):
        first=self
        while first.next!= None:
                first=first.next
        el_to_add=Node()
        el_to_add.value = val
        first.next=el_to_add
    def _del_all(self):
        return None
    def _add_to_beg(self,val):
        tmp=Node(val)
        tmp.value=val
        if self.value!=None:
            tmp.next=self
            print("S")
            return tmp
        else:
            tmp.next=None
            return tmp
    def _add_to_end_list(self,lista_to_add):
        if self == None:
            return lista_to_add
        else :
            last_lista=self
            last_lista.next=lista_to_add
            return lista_to_add

def zad_7(tab_of_lists,k):
    #Need to build the heap from first list elements
    tab_tmp=[None]*(len(tab_of_lists)+1)
    tab_tmp[0]=int (len(tab_of_lists)-1)
    for i in range(len(tab_of_lists)-1):
        tab_tmp[i+1]=tab_of_lists[i]
    tab_tmp=BuildHeap_min(tab_tmp)
    print(tab_tmp[1].value)
    tab_to_ret=[0]*(len(tab_of_lists)*k)
    ind_in_ret=0
    while tab_tmp[0]!=0:
        tab_to_ret[ind_in_ret]=tab_tmp[1].value
        ind_in_ret+=1
        if tab_tmp[1].next!=None:
            tab_tmp[1]=tab_tmp[1].next
            tab_tmp=heapify_min(tab_tmp,1)
        elif tab_tmp[1].next==None:
            tab_tmp[1]=tab_tmp[tab_tmp[0]]
            tab_tmp[0]-=1
            tab_tmp=heapify_min(tab_tmp,1)
    return tab_to_ret

X=Node()
Y=Node()
X=X._in(4)
Y=Y._in(3)
print(zad_7([X,Y],3))




    

    










