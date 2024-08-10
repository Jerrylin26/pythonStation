"""

#按大小輸出
list=[]
a = int(input("請輸入3個數值，第一個:"))
b = int(input("第二個:"))
c = int(input("最後一個:"))
list.append(a)
list.append(b)
list.append(c)

for item in sorted(list):
    print(item)
    
#----------------------------------------------------
    
#二亂數1~100，隨機選10個數，僅印出質數


import random

listbefore = []
listafter = []
for item in range(10):
    a = random.randint(1, 100)
    listbefore.append(a)
print("10 num:",listbefore)

for i in listbefore:
    if i==2: #由於當for b in range(2,i):得i=2時，程式不會執行，所以直接加入質數串列
        listafter.append(i)
    for b in range(2,i):
        if i%b==0:
            break
    
        elif b==i-1: #若能跑到i-1，代表沒有除數是1跟子自己以外了。
        #例:12的除數[1,2,3,4,6,12] ,7以上不會出現除數，除12(本身)
            listafter.append(i)
print("質數:",sorted(listafter))

"""
#----------------------------------------------------

#輸入數字，直到超過50。並輸出前面(數值平方)的加總 sum squared

list = []
sum = 0
while True:
    i = int(input("輸入數值:"))
    if i>50:
        break
    list.append(i*i)
    sum += i*i
    
print()
print("大於50停止")
print("平方",list)
print("平方和:",sum)

    

    
    

    
    
    