def Select_sort(tab):
    for j in range(0,len(tab)): #Will Be Searching min for this place (for j)
        #Repeat this operation for every possible place
        min = tab[j]
        min_index=j
        for i in range(j,len(tab)): # The Search
            if tab[i]<min:
                min=tab[i]
                min_index=i
        #Switching the j and the min_el in the current array
        tab[j],tab[min_index]=tab[min_index],tab[j] 
    return tab

print(Select_sort([5,2,1,3,4,1,1,15]))
    
            