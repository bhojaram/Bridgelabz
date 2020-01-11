import datetime
import math
import sys
import numpy as num
import array as arr
import random
#import time

#checking Anagram

def Anagram(str1, str2):
    a= len(str1)
    b= len(str2)
    #comparing length
    if a != b :
        return 0
    else :
        #sorting both string using inbuilt function
        c= sorted(str1)
        d= sorted(str2)
        for i in range(0 ,a):
            if c[i] != d[i]:
                return 0
            return 1    

             

#Bubblesort 

def Bubblesort(arr, n):
    for i in range (0,n-1):
       for j in range (0, n-i-1):
           #logic for swapping
           if (arr[j]>arr[j+1]):
               temp = arr[j]
               arr[j]= arr[j+1]
               arr[j+1]=temp                

#Insertationsort


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp

def Insertationsort(a):
    for i in range (0,len(a)-1):
        min = a[i+1]
        j=i
        while j>=0 and min< a[j]:
            #logic for swapping
            temp= min
            a[j+1]= a[j]
            j= j-1
        a[j+1]= min
            
    return a

#Selectionsort

def Selectionsort(arr, n):
    for i in range (0,n-1):
        min = i
        for j in range (i+1, n):
           if (arr[j] < arr[min]):
               #logic for swapping
               temp = arr[min]
               arr[min]= arr[j]
               arr[j]=temp    

#Permutationstring

def permute(s, l, h): 
    if l==h: 
        print(s) 
    else: 
        for i in range(l,h+1):
            #swapping 
            s[l],s[i] = s[i],s[l] 
            permute(s, l+1, h)
            #backtracking  
            s[l], s[i] = s[i], s[l] 

#Prime no. range in 0-1000  
def Primecount(l,h):
    for val in range(0,h+1):
        if val > 1 :
            for i in range(2,val):
            if val % i==0:
                #checking of factors of l  
                break
            else :
                print(val)
                    
            
                
#finding a no. using binary sort
def Binarysearch(a,l,h):
    #for one element i.e. terminating condition
    if l == h:
        if a == arr[l]:
            print(a)
        else:
            print("not present")    
    else:
        mid = (l+h) / 2
        if a < mid:
            #a should be in range  l to mid-1
            Binarysearch(a,l,mid-1)
        elif a > mid:
            #a should be in range mid+1 to h
            Binarysearch(a,mid+1,h)
        else:
            #when a== mid
            print(mid) 

#String relacement programme
def Stringreplace(str1):
    print(str1.replace("am" , "were", )) 

#Powerof2 programme
def Poweroftwo(n):
    for i in range(0,n+1):
        print("the power is ")
        #using python inbuilt function i.e. pow()
        print( pow(2,i)) 

#Harmonic series printing
def Harmonic(n):
    #taking initial harmonic sum as 1
    hsum=1 
    for i in range(2,n+1):
        hsum = hsum + (1/i)
        print(hsum) 

#calculation of primefactors 

def Primefactor(num):
    #printing 2 as it`s  a prime number
    while num % 2 == 0:
        print(2)
        num =num / 2
    #now checking if every prime no. divided by num
    # also printing no. 
    #last argument is for stepping of 2
    for i in range (3,int(math.sqrt(num))+1 ,2):
        while num % i == 0:
            print(i)
            num = num /i  
    #for num after factorizing
    if num > 2:
        print(num)

#calculating time elapseed in stopwatch
def Stopwatch(start_time,end_time):
    elapsed_time= start_time - end_time()
    print(elapsed_time) 


#flip coin problem

def Flipcoin(a):
    #initilising count variables
    counthead=0
    counttail=0
    for i in range (0,len(a)+1):
    
        if(a[i]> 0.5):
            counthead = counthead+1
        else :
            counttail = counttail+1
#calculate percentage and printing        
    percentage = (counthead / (len(a)))*100
    print(percentage) 
    percentage = (counttail / (len(a)))*100
    print(percentage)  


#Gambler programme
def Gambler(stake,goal,trails):
    #initilising count variables
    win_count=0
    loss_count=0
    if stake >= 0  or goal == stake:
        #system generating random numbers
        if random.randint(0,1) < 0.5:
            stake = stake-1
            loss_count = loss_count+1
        else:
            stake = stake+1
            win_count = win_count+1
    #calculating percentage
        percentage_win= (win_count/trails)*100
        print(percentage_win)
        percentage_loss= (loss_count/trails)*100
        print(percentage_loss)  

#finding distinct coupon numbers
def Couponnumber(a):
    count=0
    for i in range(0,len(a)+1):
        if  random.randint(0,20) == a[i]:
            count= count+1 
            print(count)                            
     

#finding leap year or mot

def Leapyear(n):
    #logic for leap year
    if ( n % 4 == 0 and  n %  100 != 0 or n % 400 == 0):
        print("Leapyear")
    else :
        print ("Not leapyear")


#finding triplets in an array
# array of distinct element

def Triplets(a):
    for i in range(0,len(a)-2):
        for j in range(i+1,len(a)-1):
            for k in range(j+1,len(a)):
                if a[i]+a[j]+a[k]== 0:
                    print(a[i],a[j],a[k]) 


#calculating distane of a point from origin
#x1,x2 is origin & y1,y2 be any point
def Distance (x1,x2,y1,y2):
     d= math.sqrt(math.pow(x2 - x1, 2) +
                math.pow(y2 - y1, 2) * 1.0)
     print("the distance is :", d)


#findingPrime no. range in 0-1000 
#and showing palendrome or not 
def Palendromerange(l,h):
    for l in range(0,h+1):
        for i in range(2,h):
            if l % i==0:
                #checking of factors of l  
                if l==i:
                    print("Not prime")
                else:
                    print(l)
                    #reversing the number
                    while l > 0:
                        rev = 0
                        rem = l%10
                        rev =rev*10+rem
                        l   =l/10
                        #comparing reverse and prime number
                        if l == rev:
                            print("The prime no. is Palendrome")
                        else:
                            print("The prime no. is not Palemdrome")
#mergesort program
def mergesort(arr,low,high):
    if low < high:
        mid = int((low+high) /2)
        mergesort(arr,low,mid)
        mergesort(arr,mid+1,high)
        i=low
        j=mid+1
        k=high
        b =arr.array('i', [])
        while i<=mid and j<=high:
            if arr[i] <= arr[j]:
                b[k]=arr[i]
                i +=1
            else:
                b[k]=arr[j]
                j +=1
            k +=1 
        while i < mid:
            b[k]=arr[i] 
            k +=1
            i +=1                                     
        while j < high:
            b[k]=arr[j]
            k +=1
            j +=1
 
        
#orderlist program
class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None
    #printing the linkedlist    
    def printlist(self):
        temp = self.head
        #traversing till the end of list
        while temp != None:
            print(temp.data)
            temp = temp.next
    #appending nodes to linkedlist
    def append(self,data):
        newnode = node(data) 
        #checking for blank list  
        if self.head is None: 
            self.head = newnode 
            return
        temp = self.head 
        while temp.next is not None: 
            temp = temp.next
              
        temp.next = newnode
    #returning size of list     
    def sizelist(self):
        temp = self.head
        sizeoflist = 0
        while temp != None:
            sizeoflist += 1
            temp = temp.next
        #print("size is :",sizeoflist)  
        return sizeoflist
    #checking for single node    
    #and delet the that node
    def pop_last(self):
        temp = self.head
        if temp.next == None:
            return temp.data
            temp = None
            self.head = None
    #delet element at given position        
    def pop(self,pos):
        temp = self.head
        length = self.sizelist()
        if pos <= 0 or pos > length:
            print("invalid position")
        elif pos == 1:
            if temp.next == None:
                temp = None
                self.head = None
            else:
                self.head = self.head.next
                temp.next = None
                
        #deleting the last node    
        elif pos == length:
            Temp = None
            while temp.next != None:
                Temp = temp
                temp = temp.next
            Temp.next = None
            temp = None
        else:
            #k is variable assign 1
            #which help Temp to point precceding node
            Temp = None
            k = 1  
            while k < pos:
                k += 1
                Temp = temp
                temp = temp.next
            Temp.next = temp.next
            temp.next = None
    #deleting a particular item        
    def remove(self,item): 
            temp = self.head
            Temp = None
            #searching for item
            while temp.data != item:
                Temp = temp
                temp = temp.next
            #removing item and making reference    
            Temp.next = temp.next
            temp.next = None
    #inserting item at given position        
    def insert(self,pos,item):
        newnode = node(item)
        temp = self.head
        #calling sizelist method
        length = self.sizelist()
        if pos <= 0 or pos > length+1:
            print("invalid position")
        #inserting at first position 
        #and incresing length    
        elif pos == 1:
            if self.head == None:
                self.head = newnode
                length += 1
            else:
                newnode.next = self.head
                self.head = newnode
        #inserting after last node        
        elif pos == length+1:
            while temp.next != None:
                temp = temp.next
            temp.next = newnode
            length += 1
        #inserting in particular position    
        else:
            k = 1
            while k < pos-1:
                k += 1
                temp = temp.next
                
            newnode.next = temp.next
            temp.next = newnode
            length += 1
    def sort(self,item):
        #checking item present or not
        #then remove it
        temp = self.head
        newnode = node(item)
        if temp.data == item:
            self.remove(item)
        temp = temp.next    
        #if item not present 
        #placing in apporiate position   
        while temp != None:
            temp = self.head
            Temp = None
            if temp.data > newnode.data:
                    Temp = temp 
                    temp = temp.next
            newnode.next = Temp.next
            Temp.next = newnode
                    
        return        
    
    def add(self,item):
        temp = self.head
        newnode = node(item)
        if temp == None:
            temp = newnode
        while temp.next == None:
            temp.next = newnode
        return        
    def convert(lst): 
        return (lst.split())     
        
    #returning index of item    
    def index(self,item):
        temp = self.head 
        pos = 0  
        while temp != None:
            if temp.data == item:
                pos += 1
            temp = temp.next
            pos += 1
    #checking for emptyness of list        
    def isEmpty(self):
        if self.head == None:
            print("List is empty")
        return
#balacing parenthesis
class stack_node :
    #creating stack nodes
    def __init__(self,data):
        self.data = data
        self.next = None
        
class stack :
    #creating empty stack with zero
    def __init__(self):
        self.top = None
        self.size = 0
    def len_stack(self):
        return self.size
        #print( "self.size")
    #checking for empty stack    
    def isEmpty(self):
        if self.top == None:
            print("stack empty")
            return
    #pushing item into stack        
    def push(self,data):
        newnode = stack_node(data)
        if self.top == None :
            self.top = newnode
        newnode.next = self.top 
        self.top = newnode
        self.size += 1
        return self.size
    #delet top element from stack    
    def pop(self):
        #pop not possible if stack is empty
        if self.isEmpty :
            print("pop not possible")
        item = self.top.data
        self.top = self.top.next 
        self.size -= 1
        return
    def peek(self):
        item = self.top.data
        print(item)
        return 
#Bank_cash_counter program
class queue_node :
    #a linkedlist of nodes
    #to create nodes for queue
    def __init__ (self,data):
        self.data = data
        self.next = None
#Q class created, head refers first element
# tail refers last element        
class queue :
    def __init__ (self):
        self.head = None
        self.tail = None
        self.size = 0
    #returning size of Queue    
    def q_size(self):
        return self.size
    #checking for empty of queue    
    def q_isEmpty(self):
        if self.head == None :
            return
    #inserting data & creating node        
    def enqueue(self,data):
        newnode = queue_node(data)
        if self.tail == None :
            #for first insertation ..
            #head,tail should refer to newnode
            self.head = newnode
            self.tail = newnode
        self.tail.next = newnode
        self.size += 1 
    #deleting checking for head                     
    def dequeue(self):
        if self.head == None :
            print("dequeue not possible")
        newnode = self.head 
        #checking for single item & delet   
        if self.head == self.tail :
            self.head = None
            self.tail= None
        #delet node & head points to next node        
        self.head = newnode.next
        self.size -= 1    
        return head.data                   
#palindrome_checker               
class dqueue_node :
    #a linkedlist of nodes
    #to create nodes for queue
    def __init__ (self,data):
        self.data = data
        self.next = None
#dQ class created, head refers first element
# tail refers last element        
class dqueue :
    def __init__ (self):
        self.head = None
        self.tail = None
        self.size = 0
    #returning size of dQueue    
    def d_size(self):
        return self.size
    #checking for empty of queue    
    def d_isEmpty(self):
        if self.head == None :
            return
    #creating list of nodes
    #i.e charcter by charcter        
    def stringToListNode(str1):
    for i in str1:
        newnode = dqueue_node(i)        
    #inserting data & creating node
    #from head/front end       
    def add_head(self,data):
        newnode = dqueue_node(data)
        if self.head == None :
            #for first insertation ..
            #head,tail should refer to newnode
            self.head = newnode
        #creating node & shifting head to back    
        newnode.next = self.head
        newnode = self.head
        self.size += 1 
    #creating node from tail/rear end    
    def add_tail(self,data): 
        newnode = dqueue_node(data)
        if self.tail == None :
            self.tail = newnode
        #adding node to next of tail     
        self.tail.next = newnode 
        self.size += 1
    #deleting checking for head                     
    def remove_head(self):
        if self.head == None :
            print("dequeue not possible")
        newnode = self.head 
        #checking for single item & delet   
        if self.head == self.tail :
            self.head = None
        #delet node & head points to next node        
        newnode.next = self.head
        self.size -= 1    
        return head.data 
     def remove_tail(self):
        if self.tail == None :
            print("dequeue not possible")
        newnode = self.tail
        temp = self.head 
        #checking for single item & delet   
        if self.head == self.tail :
            self.tail= None
        #traverse till end of list
        #making reference to previous of last node  
        while temp != None :
            Temp = temp
            temp = temp.next
        Temp = self.tail           
        Temp = temp = None 
        self.size -= 1    
        return tail.data                   
#binary_search tree implementation
class node:
    def __init__(self,data) :
        #taking 2 pointers for bst
        #left of root & right of root
        self.data = data
        self.left_child = None
        self.right_child = None
class binary_search_tree :
        def __init__(self) :
            #initilising root as null
            self.root = None   
        def add(self,data) :
            #inserting new node to root
            newnode = node(data) 
            if self.root == None :
                self.root = newnode
            else :
                #if root already present calling method
                self.insert(self,newnode) 
        def insert(self,data,newnode) :
            #comparing root and newnode
            # if samller,place  at left child            
            if self.root.data < newnode.data :
                if self.left_child == None :
                   self.left_child = newnode
                else :
                   #if left child already present
                   #calling insert method
                   self.left_child.insert(newnode)
            return       
            else :
               #if bigger,place at right side 
               if self.root.data > newnode.data :
                  if self.left_right == None :
                    self.left_right = newnode
                  else :
                    #calling insert method  
                    self.right_child.insert(newnode)
                return    
        def print_tree(self) :
            #printing left sub_tree
            if self.left_child :
                self.print_tree()
            print self.data
            #printing right sub_tree
            if self.right_child :
                self.print_tree()
            print self.data                     
#finding prime numbers in range
#then storing in 2D array
def primeStore2D(l,h):
    k = []
    for val in range(0,h+1):
        if val > 1 :
            for i in range(2,val):
            if val % i==0:
                #checking of factors of l  
                break
            else :
                lst.append(val)
    for j in range(0,len(lst),100) :
        k.append(lst[j:100+j])           
    print(lst)
    print(k)
#finding prime no. that are Anagram
#& storing in 2D array
    
def primeAnagramStore2D(l,h):
    k = []
    for val in range(l,h+1):
        if val > 1:
            for i in range(2,val):
                if val % i==0: 
                    break
            else:
                k.append(val)
                
    primeAnagram(k)
def primeAnagram(prime_list):
    primeAangramList = []
    for m in prime_list:
        for n in prime_list:
            if (m != n) and (sorted(str(m)) == sorted(str(n))):
                primeAnagramList.append(m)
    print(primeAnagramList)    
                   