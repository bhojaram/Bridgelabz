import sys
sys.path.append('/home/user/Bridgelabz')
from Utility.utility import Gambler

#takinng user input
stake=input("entre the stake amount :")
goal=input("enter the goal amount :")
trails=("entre the no. of trails")
#function calling
Gambler(stake,goal,trails)