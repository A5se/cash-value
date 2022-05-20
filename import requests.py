import requests
from bs4 import BeautifulSoup
import time
from time import gmtime, strftime
import emoji
import smtplib
from email.mime.text import MIMEText
from email.header import Header

print('Exchange Rates v1.0')
print(emoji.emojize('Сделано с :blue_heart:\n\n'))


class CurrencyRate:

    __login: str = 'user@gmail.com'
    __password = ''

    DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk00z4iQbIPw7txjcpJasYv7dK_NZCA%3A1585477287016&ei=p3aAXtFL3YCTvg__57L4DQ&q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&gs_lcp=CgZwc3ktYWIQDDIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQR1AAWABgrzdoAHAEeACAAQCIAQCSAQCYAQCqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwiRu_eTu7_oAhVdwMQBHf-zDN8Q4dUDCAs'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    current_currency_rate: float = 0
    currency_deviation: float = 1.0
    mail_to: str = ''

    def __init__(self, mail_to: str = ''):
        self.current_currency_rate = self.get_currency_rate()
        self.mail_to = mail_to

    def __now(self):
        return strftime("%Y-%m-%d %H:%M:%S", gmtime())

    def get_currency_rate(self):
        full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": "2"})
        return float(convert[0].text.replace(',', '.'))

    def check_currency(self):
        currency = self.get_currency_rate()
        if currency >= self.current_currency_rate + self.currency_deviation:
            print(emoji.emojize("Курс доллара сильно вырос :thums_up:"))
        elif currency <= self.current_currency_rate - self.currency_deviation:
            print(emoji.emojize("Курс доллара сильно упал :-1:"))
        currency_rate_message = f"{self.__now()} курс: 1 доллар = {currency} руб."
        print(currency_rate_message, f'\n\nОтправляем на почту {self.mail_to}')
        self.__send_mail(currency_rate_message)
        # time.sleep(3)
        # self.check_currency()

    def __send_mail(self, text: str):
        server = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
        server.set_debuglevel(1)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.__login, self.__password)

        message = MIMEText(text, 'plain', 'utf-8')
        message['Subject'] = Header(f'Курс валют $ --> {self.__now()}', 'utf-8')
        message['From'] = self.__login
        message['To'] = self.mail_to
        print(self.mail_to)
        server.sendmail(message['From'], message['To'], message.as_string())
        server.quit()


currency = CurrencyRate('user@mail.ru')
currency.check_currency()