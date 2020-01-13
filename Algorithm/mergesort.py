import sys
sys.path.append('/home/user/Bridgelabz')
from Utility.utility import mergesort
arr=[3,6,7,2,9,5]  
n= len(arr)
#calling mergesort method
mergesort(arr,0,n)
#printing  sorted array
print("the sorted array is ")    
for i in range (0 ,n):
    print(arr[i])    