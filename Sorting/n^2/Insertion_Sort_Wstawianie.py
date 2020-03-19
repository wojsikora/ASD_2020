def ins_sort_popr(tab):
    for i in range(1,len(tab)):   #Element to insert
        j=i-1   
        val=tab[i]
        while j>=0 and tab[j]>val:  #Finding place to insert, "przesuwam" in the back the array
            tab[j+1]=tab[j]
            j-=1
        tab[j+1]=val    #Inserting the element we wanted to insert
    return tab

print(ins_sort_popr([6,5,4,3,7,1]))