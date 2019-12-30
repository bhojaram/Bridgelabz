import sys
sys.path.append('/home/user/Bridgelabz')
from Utility.utility import Bubblesort

arr=[3,6,7,2,9,5]  
n= len(arr)
Bubblesort(arr,n)
#printing  sorted array
print("the sorted array is ")    
for i in range (0 ,n-1):
    print(arr[i])         