import sys
sys.path.append('/home/user/Bridgelabz')
from Utility.utility import stack
if __name__=='__main__':
    s = stack()
    exp = input("enter the expression :")
    for i in exp :
        if i == '(':
            s.push(i)   
        elif i == ')':
            s.pop(i)
    if s.isEmpty == True:
        print("expression is balanced")