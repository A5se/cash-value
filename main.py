import requests
from bs4 import BeautifulSoup
import time
def ass():
    while True:
        class Currency:
            DOLLAR_RUB = 'https://www.google.com/search?q=dollar+ruble&ei=a_WUYdbbIYWTrwT19opw&oq=dollar+r&gs_lcp=Cgdnd3Mtd2l6EAMYADIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIOCC4QgAQQxwEQowIQyQMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6DgguEIAEELEDEMcBEKMCOhIILhCABBCxAxDHARDRAxAKEAE6BQgAELEDOgsILhCABBDHARDRAzoHCAAQsQMQQzoECAAQQzoLCAAQgAQQsQMQgwE6CgguEMcBEKMCEEM6BAguEEM6DQguELEDEMcBEKMCEENKBAhBGABQAFiHEGCOG2gAcAJ4AIABkwGIAdsGkgEDMy41mAEAoAEBwAEB&sclient=gws-wiz'
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}

            current_converted_price = 0
            difference = 0.05
            
            def __init__(self):
                self.current_converted_price = float(self.get_currency_price().replace(",", "."))

            def get_currency_price(self):
                full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)
                soup = BeautifulSoup(full_page.content, 'html.parser')
                convert = soup.findAll("span", {"class":"DFlfde","class":"SwHCTb","data-precision": 2})
                return convert[0].text
            def check_currency(self):
                currency = float(self.get_currency_price().replace(",", "."))
                if currency >= self.current_converted_price + self.difference:
                    print("Курс сильно вырос, может пора что-то делать")
                elif currency <= self.current_converted_price - self.difference:
                    print("Курс сильно упал, может пора что-то делать")
                print("Сейчас курс 1 доллара к рублю = " + str(currency))
                


        class btcCurrency:
            DOLLAR_RUB = 'https://ru.investing.com/crypto/bitcoin/btc-usd'
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}

            current_converted_price = 0
            difference = 0.05
            
            def __init__(self):
                
                self.current_converted_price = self.get_currency_price().replace(" ","")
                self.current_converted_price = self.get_currency_price().replace(".","")
                self.current_converted_price = float(self.get_currency_price().replace(",",""))

            def get_currency_price(self):
                full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)
                soup = BeautifulSoup(full_page.content, 'html.parser')
                convert = soup.findAll("span", {"class":"pid-945629-last"})
                return convert[0].text
            def check_currency1(self):
            
                currency1 = float(self.get_currency_price().replace(",",""))
                if currency1 >= self.current_converted_price + self.difference:
                    print("Курс сильно вырос, может пора что-то делать")
                elif currency1 <= self.current_converted_price - self.difference:
                    print("Курс сильно упал, может пора что-то делать")
                print("Сейчас курс 1 BTC/DOLLAR.USA = " + str(currency1))
                
                
        
        currency = Currency()
        currency.check_currency()
        currency1 = btcCurrency()
        currency1.check_currency1()
            
ass()