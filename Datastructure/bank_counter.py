import sys
sys.path.append('/home/user/Bridgelabz')
from Utility.utility import queue 
#main method   
if __name__== '__main__':
    q = queue()
    n = int(input("enter the no. of person"))
    #taking bank balance & indivisual amount
    bank_balance = 10000
    m = [100,200,300,]
    k = 0
    while k < n :
        #inserting person into Q
        q.enqueue(input("enter the name of person :"))
        k += 1
    def check_option() :
        for i in range(n) :
            choice_input = input(Withdrawl is W / Depositis is  D)
            #calling deposit & withdrawl method
            if choice_input == 'D' :
                deposit(i) 
            elif coice_input == 'W' :
                withdrawl(i)

    def deposit(i) :
        d_amount = int(input("enter deposit amount :"))
        #increasing both amount & poping the person
        m[i] == m[i] + d_amount
        bank_balance += d_amount
        q.dequeue()
    def withdrawl(i) :
        w_amount =  int(input("enter withdrawl amount :"))
        #checking for sufficient amount
        if w_amount < m[i] :
            m[i] = m[i]- w_amount
            bank_balance -= w_amount
        else :
            print("insufficient fund")
        q.dequeue() 
#printing indivisual amount        
print(m)
print(bank_balance)               
