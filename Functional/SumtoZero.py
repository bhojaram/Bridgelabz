def SumtoZero(a):
    for i in range(0,len(a)-2):
        for j in range(i+1,len(a)-1):
            for k in range(j+1,len(a)):
                if a[i]+a[j]+a[k]== 0:
                    print(a[i],a[j],a[k])                   

            
       

a= [-1,-2,0,1,2,]
SumtoZero(a)


















