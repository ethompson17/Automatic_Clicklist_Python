from bs4 import BeautifulSoup
import requests
import selenium
from selenium import webdriver



# Tomatoes
class Roma_Tomatoes:

    def kroger_roma_tomatoes(self):
        kroger_url = 'https://www.kroger.com/p/roma-tomato/0000000004087?fulfillment=PICKUP'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
        kroger_roma_tomatoes_page = requests.get(kroger_url, headers=headers)
        kroger_roma_tomatoes_soup = BeautifulSoup(kroger_roma_tomatoes_page.content, 'html.parser')
        kroger_roma_tomatoes_price = kroger_roma_tomatoes_soup.find('span', class_='kds-Text--l mr-8 text-default-900 ProductDetails-sellBy').text

        print(kroger_roma_tomatoes_price)

    def meijer_roma_tomatoes(self):
        meijer_url = 'https://www.meijer.com/shopping/product/roma-tomato/4087.html'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
        meijer_roma_tomatoes_page = requests.get(meijer_url, headers=headers)
        meijer_roma_tomatoes_soup = BeautifulSoup(meijer_roma_tomatoes_page.content, 'html.parser')
        meijer_roma_tomatoes_price = meijer_roma_tomatoes_soup.select('span', class_ = 'product-info__description')

        print(meijer_roma_tomatoes_price)

    def gordon_roma_tomatoes(self):
        gordon_url = 'https://gfsstore.com/products/675780/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
        gordon_roma_tomatoes_page = requests.get(gordon_url)
        gordon_roma_tomatoes_soup = BeautifulSoup(gordon_roma_tomatoes_page.content, 'html.parser')
        gordon_roma_tomatoes_price = gordon_roma_tomatoes_soup.find('span', class_='unit_price').text

        print(gordon_roma_tomatoes_price)

    def buschs_roma_tomatoes(self):
        buschs_url = 'https://www.buschs.com/shopping/produce'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
        buschs_roma_tomatoes_page = requests.get(buschs_url)
        buschs_roma_tomatoes_soup = BeautifulSoup(buschs_roma_tomatoes_page.content, 'html.parser')
        buschs_roma_tomatoes_parent = buschs_roma_tomatoes_soup.find_all('div', class_ = 'item-block col-xs-12 col-sm-6 col-md-2')

        print(buschs_roma_tomatoes_parent)


rt = Roma_Tomatoes()
#list(rt.kroger_roma_tomatoes(), rt.gordon_roma_tomatoes())

rt.kroger_roma_tomatoes()
rt.meijer_roma_tomatoes()
rt.gordon_roma_tomatoes()
rt.buschs_roma_tomatoes()



# meijer_url = 'https://www.meijer.com/shopping/product/roma-tomato/4087.html'
# buschs_url = 'https://www.buschs.com/shopping/produce'
# gordon_url = 'https://gfsstore.com/products/675780/'
# walmart_url = 'https://www.walmart.com/ip/Roma-Tomatoes/44390944'
