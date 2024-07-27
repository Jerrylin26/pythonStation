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
    
    #隨機選數字
    if a == 4:
        while(True):
            num_1 = random.randint(2,100)
            num_2 = random.randint(2,num_1)
            if num_1%num_2==0 and num_1!=num_2:
                break
        
        #除法
        b = int(input(str(num_1)+"÷"+str(num_2)+"="))
        if b == num_1/num_2:
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
            print("bad")
    print("-"*30)
    #離開
    if a == 5:
        break


