def Bubble_sort(tab):
    for i in range(len(tab)):
        for j in range(0,len(tab)-i-1):
            if tab[j]>tab[j+1]:
                tab[j],tab[j+1]=tab[j+1],tab[j]
    return tab

print(Bubble_sort([4,5,7,1,2,4,9]))
