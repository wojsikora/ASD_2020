# Hoare polega na częściowym podziale bez ustawienia pivota, więc 
# rozbijając tab musimy włączyć piv_index
def Hoare_part(tab,low,high):
    pivot=tab[low]
    i=low-1
    j=high+1
    while 1:
        while 1:
            i+=1
            if tab[i]>=pivot:break
        while 1:
            j-=1
            if tab[j]<=pivot:break
        # Jesli indeksy nie nachodza to swap
        if i<j:
            tab[i],tab[j]=tab[j],tab[i]
        else:
        #wracamy wartosc j ktora jest ustawiona na el kotory "presortowany"
            return j

def q_sort(tab,low,high):
    if low<high:
        piv_idex=Hoare_part(tab,low,high)
        q_sort(tab,low,piv_idex)
        q_sort(tab,piv_idex+1,high)
tab=[17,3,17,20,0,17]
q_sort(tab,0,5)
print(tab)