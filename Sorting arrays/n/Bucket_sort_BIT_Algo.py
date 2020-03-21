def Bucket_sort(tab,n): #n is the max_index in one bucket 
    #The Bucket sort algorithm is based on
    #Simple idea that elements in range (0,1] are easy to sort
    #And we will be dividing them in the same principle
    max_el=max(tab) # O(n)
    buckets=[[] for _ in range(n+1)]
    for num in tab:
        num_norm=num/max_el
        buckets[int (n*num_norm)].append(num)
    for i in range(n):
        buckets[i]=sorted(buckets[i])
    #Łączenie
    out=[]
    for i in range(n):
        for j in range(len(buckets[i])):
            out.append(buckets[i][j])
    return out


print(Bucket_sort([0.1,0.15,0.18,0.11,0.5],10))


