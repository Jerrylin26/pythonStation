
#選擇項數b
b = int(input("請輸入[費氏數列]:"))

#預設[1,1]
a =[1,1]
i = 1


while(True):
    #a[i+1] = a[i-1] + a[i] 遞迴公式
    a.append(a[i-1] + a[i])
   
    i +=1
    if i == b+1:
        print(a)
        sum = 0
        for x in range(b+2): 
            sum +=a[x]
            
        print("1+.....+",a[b+1],"=",sum)
        break







