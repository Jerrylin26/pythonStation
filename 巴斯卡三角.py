# 巴斯卡三角

input = int(input("請問要幾階的巴斯卡三角:"))
ans=[]
if input==1:
    print(1)
else:
    for a in range(1,input+1):
        for b in range(1,a+1):
           
            c = 1
            for i in range(1,a):
                c *=i
            d = 1
            for i in range(1,b):
                d *=i
            e = 1
            for i in range(1,a-b+1):
                e *=i
            #num = (a-1)!/(b-1)!(a-b)!
            num = int(c/(d*e)) #轉整數
            ans.append(num)
    #print(ans)
    for x in range(1,input+1):
        print(" "*(input-x+10),end=" ")
        for i in range(x):
            y = ans.pop(0)
            print(y,end=" ")
        print()
    

"""
#4! 4*3*2*1
c=1
for i in range(1,4+1):
    c *=i
"""

"""
三角形
for x in range(1,input+1):
    print(" "*(input-x)+"*"*(x*2-1))
"""
































