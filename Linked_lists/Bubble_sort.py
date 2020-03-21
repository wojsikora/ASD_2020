class Node():
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next
class LinkedList():

    def __init__(self,first=None,last=None):
        self.first=first
        self.last=last
    def make_from_array(self,tab):
        if len(tab)==0:return
        self.first=Node(tab[0])
        p = self.first
        self.last=p
        for i in range(1,len(tab)):
            q=Node(tab[i])
            p.next=q
            p=q
            self.last=p
    def print_list_as_tab(self):
        if self.first==None:return
        tmp=self.first
        tab_to_ret=[]
        while tmp!=self.last:
            tab_to_ret.append(tmp.value)
            tmp=tmp.next
        tab_to_ret.append(tmp.value)
        return tab_to_ret
    def print_to_console(self):
        tmp=self.first
        while tmp!=None:
            print(tmp.value)
            tmp=tmp.next
    def add_to_end(self,node_to_add):
        tmp=self.last
        tmp.next=node_to_add
        self.last=node_to_add
    def add_to_beg(self,node_to_add):
        tmp=self.first
        node_to_add.next=tmp
        self.first=node_to_add
    def switch(self,prev,f):
        s=f.next
        if s==None:return
        #First one
        if prev==None and f==self.first:
            self.first=s
        if s.next==None:
            self.last=f
        f.next=s.next
        s.next=f
def switch(prev,l1,l2):
    prev.next=l2
    l1.next=l2.next
    l2.next=l1
    return l2
def Bubble_sort(first):
    length=first._len()
    wartownik = Node()
    wartownik.value=0
    wartownik.next=first
    tmp=first
    for _ in range(length-1):
        tmp = wartownik.next
        prev=wartownik
        while tmp.next != None:
            #print(tmp.next)
            if tmp.value>tmp.next.value:
                switch(prev,tmp,tmp.next)
                prev=prev.next
            else:
                prev=prev.next
                tmp=tmp.next      
    #Usuwanie wartownika
    wartownik=wartownik.next
    return wartownik