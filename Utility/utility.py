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
    for l in range(2,h+1):
        for i in range(2,h):
            if l % i==0:
                #checking of factors of l  
                if l==i:
                   print(l)
                else:
                    break
            else:
                print("not prime")
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
                              
#linkedlist program
class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None
    def printlist(self):
        temp=self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next
     #appending item/data to linkedlist       
    def append(self,data):
        newnode = node(data) 
          
        if self.head is None: 
            self.head = newnode 
            return
        temp = self.head 
        while temp.next is not None: 
            temp = temp.next
              
        temp.next = newnode 
    #adding new item in linkedlist    
    def add(self,item):
        newnode = node(item)
        temp=self.head
        while temp.next != None:
            temp = temp.next
        temp.next = newnode    
    #searching for item    
    def search(self,item):
        temp = self.head 
        while temp != None:
            if temp.data == item:
                print("item is present")
                break
            temp = temp.next
        return  
    #calculating size of linkedlist    
    def sizelist(self):
        temp = self.head
        sizeoflist = 0
        while temp != None:
            sizeoflist += 1
            temp=temp.next
        #print("size is :",sizeoflist)
    #checking emptiness of linkedlist    
    def isEmpty(self):
        if self.head == None:
            print("List is empty")
        return
    #returning index of item    
    def index(self,item):
        temp = self.head 
        pos = 0  
        while temp != None:
            if temp.data == item:
                pos += 1
            temp = temp.next
            pos += 1
    #delet the last node          
    def pop_last(self):
        temp = self.head
        if temp.next == None:
            return temp.data
            temp = None
            self.head = None
    #delet at a given position        
    def pop(self,pos):
        temp = self.head
        length = self.sizelist(self)
        if pos <= 0 or pos > length:
            print("invalid position")
        elif pos == 1:
            if temp.next == None:
                temp = None
                self.head = None
            else:
                self.head = self.head.next
                temp.next = None
        elif pos == length:
            Temp = None
            while temp.next != None:
                Temp = temp
                temp = temp.next
            Temp.next = None
            temp = None
        else:
            Temp = None
            k = 1
            while k < pos:
                k += 1
                Temp = temp
                temp = temp.next
            Temp.next = temp.next
            temp.next = None
    def remove(self,item): 
            temp = self.head
            Temp = None
            while temp.data != item:
                Temp = temp
                temp = temp.next
            Temp.next = temp.next
            temp.next = None
    #insertation at given position            
    def insert(self,pos,item):
        newnode = node(item)
        temp = self.head
        length = self.sizelist()
        #checking for invalid position
        if pos <= 0 or pos > length + 1:
            print("invalid position")
        #insertation at beginning    
        elif pos == 1:
            if self.head == None:
                self.head = newnode
                length += 1
            else:
                newnode.next = self.head
                self.head = newnode
        #insertation at last        
        elif pos == length + 1:
            while temp.next != None:
                temp = temp.next
            temp.next = newnode
            length += 1
        #insertation at random positioion    
        else:
            k = 1
            while k < pos-1:
                k += 1
                temp = temp.next
                
            newnode.next = temp.next
            temp.next = newnode
            length += 1
        
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
        



            
               
                 