import array as arr
a = arr. array( 'f', [0.1, 0.2,0.6,0.7,0.4])
#initilising count variables
counthead=0
counttail=0
for i in range (len(a)):
    
    if(a[i]> 0.5):
        
        counthead = counthead+1
       
    else :
        counttail = counttail+1
#calculate percentage and printing        
percentage = (counthead / (len(a)))*100
print(percentage) 
percentage = (counttail / (len(a)))*100
print(percentage)    
