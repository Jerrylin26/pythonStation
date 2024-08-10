import random

print("     \n         四則運算\n")
while(True):

    #選四則運算
    while(True):
        a = int(input("1:+  2:-  3:×  4:÷  5:離開遊戲  "))
        if 1 <= a <=5:
            break
        else:
            print("睜大眼睛")
    
   
    """除數不要2或3的方法，解決題目過於簡單的問題
    if a == 4:
        while(True):
            num_1 = random.randint(4,100)
            num_2 = random.randint(4,num_1)
            if num_1%num_2==0 and num_1!=num_2:
                break
    """
    
   #隨機選數字
    

    if a == 4:
        num_2 =[] #除數的串列
        
        while True:
            num_1 = random.randint(3,100)
            for i in range(1,(num_1)+1): 
                if num_1 % i ==0:
                    num_2.append(i)
            
            if len(num_2) !=2:
                print(num_1,"的除數有:",num_2)
                break
            else:
                num_2.clear() #若是質數，則不用它
         
        #隨機選一除數，剔除首尾1跟自己
        ran = random.randint(1,len(num_2)-2) 
            
 
        #除法
        b = int(input(str(num_1)+"÷"+str(num_2[ran])+"="))
        if b == num_1/num_2[ran]:
            print("good")
        else:
            print("bad")
           
    
    elif a==1 or a==2 or a==3:
        num_1 = random.randint(1,100)
        num_2 = random.randint(1,100)
    
    #加法
    if a == 1:
        b = int(input(str(num_1)+"+"+str(num_2)+"="))
        if b == num_1+num_2:
            print("good")
        else:
            print("bad")
    #減法
    elif a ==2:
        b = int(input(str(num_1)+"-"+str(num_2)+"="))
        if b == num_1-num_2:
            print("good")
        else:
            print("bad")
    #乘法
    elif a == 3:
        b = int(input(str(num_1)+"×"+str(num_2)+"="))
        if b == num_1*num_2:
            print("good")
        else:
            print("bad，很難吧!!!")
    print("-"*30)
    #離開
    if a == 5:
        break


