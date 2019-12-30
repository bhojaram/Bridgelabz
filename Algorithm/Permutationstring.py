import sys
sys.path.append('/home/user/Bridgelabz')
from Utility.utility import permute

string = list("ABC")
print(string)
n = len(string)
s = list(string)
permute(s, 0, n)