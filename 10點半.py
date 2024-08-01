

#串列+迴圈
#4花色 各13張 52
#各種花色1-13
#不考慮花色，產生52個號碼進來
#10點半
#籌碼50點(chips): 玩一次10點 
#賠率:除過五關且10.5的狀況下賠率1:3;其餘皆賠率1:2
import random

card =[]



for i in range(4):
    for n in range(1,14):
        if n >10:
            card.append(0.5)
        else:
            card.append(n)

for i in range(200):
    start = random.randint(0, 51)
    end = random.randint(0, 51)
    card[start], card[end] = card[end], card[start]


#print(card)

chip = 50 #籌碼
time =0 #一副牌玩的次數

while True:

    if time ==3: #玩3次重洗牌
        
        for i in range(4):
            for n in range(1,14):
                if n >10:
                    card.append(0.5)
                else:
                    card.append(n)
    
        for i in range(200):
            start = random.randint(0, 51)
            end = random.randint(0, 51)
            card[start], card[end] = card[end], card[start]


    #新的一局
    q =input("是否要玩10點半?(y/n):")
    if q =="n":
        break
    chip -= 10 #玩一次10點
    time += 1 #第一次
    com =[]
    player = []
   
    
    com.append(card.pop())
    player.append(card.pop())
    count = 1 #關數
    while True:
        print('玩家目前點數:',sum(player))
        if sum(player)>=10.5 or count ==5:
            break
        q =input("是否要補牌?(y/n):")
        if q =="n":
            break
        number = card.pop()
        print("點數:",number)
        player.append(number)
        count += 1
        
    if sum(player)>10.5:
        print("Lost")
    elif sum(player)==10.5 and count !=5:
        print("Win")
        chip +=20 #賠率1:2
    elif sum(player)< 10.5 and count ==5:
        print("Win")
        chip +=20 #賠率1:2
    elif sum(player) ==10.5 and count ==5:
        print("Win")
        chip +=30 #賠率1:3
        
    else:
        while True:
            print()
            print('莊家目前點數:',sum(com))
            
            if sum(com)>=10.5 or sum(com)>= sum(player):
                break
            
            number = card.pop()
            print("點數:",number)
            com.append(number)
    
        if sum(com)>= sum(player) and sum(com)<=10.5:
            print("Lost")
        else :
            print("莊家報了，Win")
            chip +=20
    if chip ==0:
        print("You're broke.\nSee you next time.")
        break
    
    print("目前籌碼:",chip)
    print("-"*30)
