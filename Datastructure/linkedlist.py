import sys
sys.path.append('/home/user/Bridgelabz')
from Utility.utility import linked_list  
        
if __name__=='__main__':
    l=linked_list()
    lst =  ["bridgelabz banglore is here"] 
    List=print(convert(lst))  
    for i in range(len(List)+1):
        add(List[i])
    l.printlist()
    
        
    