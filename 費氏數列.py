
#選擇項數b
b = int(input("請輸入[費氏數列---第n項 *第0項為1,第1項為1,第2項為2]:"))

#預設[1,1,2]
a =[1,1,2]
i = 2


while(True):
    #a[i] = a[i-2] + a[i-1] 遞迴公式
    a.append(a[i-1] + a[i])
   
    i +=1
    if i == b:
        print(a)
        sum = 0
        for x in range(b+1): 
            sum +=a[x]
            
        print("1+.....+",a[b],"=",sum)
        break
    
