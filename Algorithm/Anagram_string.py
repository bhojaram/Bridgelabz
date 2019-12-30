import sys
sys.path.append('/home/user/Bridgelabz')
from Utility.utility import Anagram    
#two string arguments
x=int(input("enter x value"))
x = Anagram("night" ,"thing")
if x==1:
    print("Anagram")
else:
    print("Not Anagram")    