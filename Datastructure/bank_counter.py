import sys
sys.path.append('/home/user/Bridgelabz')
from Utility.utility import queue 
#main method   
if __name__== '__main__':
    q = queue()
    #entering the deposit amounts 
    q.enqueue(500)
    q.enqueue(600)
    #occuring withdrawl amount 
    q.dequeue()
    print("dequeue item is ", q.dequeue())        