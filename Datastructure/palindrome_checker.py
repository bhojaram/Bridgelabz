import sys
sys.path.append('/home/user/Bridgelabz')
from Utility.utility import dqueue 
#main method   
if __name__== '__main__':
    q = dqueue()
    str1 = "abba"
    length = q.d_size()
    q.stringToListNode(str1)
    while d.d_size() > 1 :
        first = d.remove_head()
        last = d.remove_tail()
        if first != last:
            print("not palindrome")
        else :
            continue
    print("palindrome")  
                          