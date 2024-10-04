import requests
from bs4 import BeautifulSoup

url = "https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates"

data = requests.get(url)
data.encoding = 'utf-8'

data = data.text

soup = BeautifulSoup(data,'html.parser')

currency = soup.find('table')
trs = currency.find_all('tr')

for row in trs:
    country_e = row.find(class_= 'col-1 col-lg-2 title-item title-en')   
    country =row.find(class_='col-auto px-3 col-lg-5 title-item')
    SER_buy = row.find(class_='BBoardRate')
    SER_sell = row.find(class_='SBoardRate')
    CER_buy = row.find(class_='CashBBoardRate')
    CER_sell = row.find(class_='CashSBoardRate')
    
    
    
    
    
    #因為tr 裡藏其他tr ，正常情況下會是None 但因為.text會轉成文字，而None不能轉文字，所以會錯
    if country!= None :
        print('幣別:',country.text.strip(),country_e.text.strip())
        print('即期匯率買入:',SER_buy.text.strip())
        print('即期匯率賣出:',SER_sell.text.strip())
        print('現金匯率買入:',CER_buy.text.strip())
        print('現金匯率賣出:',CER_sell.text.strip())
        print()
    
    