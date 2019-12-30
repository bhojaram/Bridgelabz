import datetime
import math
import sys
import numpy as num
import array as arr

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
    for l in range(0,h+1):
        for i in range(2,h):
            if l % i==0:
                #checking of factors of l  
                if l==i:
                    print("Not prime")
                else:
                    print(l)

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

            
               
                 