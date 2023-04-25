from bs4 import BeautifulSoup
import requests
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# from pathlib import Path
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from django.conf import settings

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}


def flipkart(name):
    try:
        global flipkart
        name1 = name.replace(" ", "+")
        flipkart = f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
        flipkart_link = flipkart
        res = requests.get(
            f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off',
            headers=headers)

        print("\nSearching in flipkart....")
        soup = BeautifulSoup(res.text, 'html.parser')

        if (soup.select('._4rR01T')):
            flipkart_name = soup.select('._4rR01T')[0].getText().strip().upper()
            if name.upper() in flipkart_name:
                flipkart_price = soup.select('._30jeq3._1_WHN1')[0].getText().strip()
                flipkart_name = soup.select('._4rR01T')[0].getText().strip()
                flipkart_image = soup.select('._396cs4')[0]
                print(flipkart_image['src'])
                flipkart_image = flipkart_image['src']
                print("Flipkart:")
                print(flipkart_name)
                print(flipkart_price)
                print("---------------------------------")

        elif (soup.select('._4ddWXP')):
                #flipkart_name = soup.select('._3Djpdu')[0].getText().strip().upper()
                #if name.upper() in flipkart_name:
                    flipkart_price = soup.select('._30jeq3')[0].getText().strip()
                    flipkart_name = soup.select('.s1Q9rs')[0].getText().strip()
                    flipkart_image = soup.select('._396cs4')[0]
                    print(flipkart_image['src'])
                    flipkart_image = flipkart_image['src']
                    print("Flipkart:")
                    print(flipkart_name)
                    print(flipkart_price)
                    print("---------------------------------")
        else:
             flipkart_price = '0'

        return flipkart_price, flipkart_name[0:50], flipkart_image, flipkart_link
    except:
        print("Flipkart: No product found!")
        print("---------------------------------")
        flipkart_price = '0'
        flipkart_image = '0'
        flipkart_name = '0'
        flipkart_link = '0'
    return flipkart_price, flipkart_name[0:50], flipkart_image, flipkart_link


def amazon(name):
    try:
        global amazon
        name1 = name.replace(" ", "-")
        name2 = name.replace(" ", "+")
        amazon = f'https://www.amazon.in/{name1}/s?k={name2}'
        amazon_link = amazon
        res = requests.get(f'https://www.amazon.in/{name1}/s?k={name2}', headers=headers)
        print("\nSearching in amazon...")
        soup = BeautifulSoup(res.text, 'html.parser')
        amazon_page = soup.select('.a-size-medium.a-color-base.a-text-normal')
        amazon_page_length = int(len(amazon_page))
        for i in range(0, amazon_page_length):
            name = name.upper()
            amazon_name = soup.select('.a-size-medium.a-color-base.a-text-normal')[i].getText().strip().upper()
            if name in amazon_name:
                amazon_name = soup.select('.a-size-medium.a-color-base.a-text-normal')[i].getText().strip()
                amazon_images = soup.select('.a-section.aok-relative.s-image-fixed-height')
                amazon_image = amazon_images[0].find_all('img', class_='s-image')[0]
                amazon_image = amazon_image['src']
                amazon_price = soup.select('.a-price-whole')[i].getText().strip().upper()
                print("Amazon:")
                print(amazon_name)
                print("₹" + amazon_price)
                print("---------------------------------")
                break
            else:
                i += 1
                i = int(i)
                if i == amazon_page_length:
                    amazon_price = '0'
                    print("amazon : No product found!")
                    print("-----------------------------")
                    break

        return amazon_price, amazon_name[0:50], amazon_image, amazon_link
    except:
        print("Amazon: No product found!")
        print("---------------------------------")
        amazon_price = '0'
        amazon_name = '0'
        amazon_link = '0'
        amazon_image = '0'
    return amazon_price, amazon_name[0:50], amazon_image, amazon_link


def gadgetsnow(name):
    try:
        global gadgetsnow
        name1 = name.replace(" ", "-")
        name2 = name.replace(" ", "+")
        gadgetsnow = f'https://shop.gadgetsnow.com/mtkeywordsearch?SEARCH_STRING={name2}'
        gadgetsnow_link = gadgetsnow
        res = requests.get(f'https://shop.gadgetsnow.com/mtkeywordsearch?SEARCH_STRING={name2}', headers=headers)
        print("\nSearching in gadgetsnow...")
        soup = BeautifulSoup(res.text, 'html.parser')
        gadgetsnow_page = soup.select('.product-name')
        gadgetsnow_page_length = int(len(gadgetsnow_page))

        for i in range(0, gadgetsnow_page_length):
            name = name.upper()
            gadgetsnow_name = soup.select('.product-name')[i].getText().strip().upper()
            if name in gadgetsnow_name:
                gadgetsnow_name = soup.select('.product-name')[i].getText().strip()
                images = soup.select('.product-img-align')[i]
                image = images.select('.lazy')[0]
                gadgetsnow_image = image['data-original']
                gadgetsnow_price = soup.select('.offerprice')[i].getText().strip().upper()
                gadgetsnow_price = "".join(gadgetsnow_price)
                gadgetsnow_price = gadgetsnow_price[1:]
                print("GadgetSnow:")
                print(gadgetsnow_name)
                gadgetsnow_price = "₹" + gadgetsnow_price
                print("---------------------------------")
                break
            else:
                i += 1
                i = int(i)
                if i == gadgetsnow_page_length:
                    gadgetsnow_price = '0'
                    print("GadgetSnow : No product found!")
                    print("-----------------------------")
                    break

        return gadgetsnow_price, gadgetsnow_name[0:50], gadgetsnow_image, gadgetsnow_link
    except:
        print("GadgetSnow: No product found!")
        print("---------------------------------")
        gadgetsnow_price = '0'
        gadgetsnow_name = '0'
        gadgetsnow_image = '0'
        gadgetsnow_link = '0'
    return gadgetsnow_price, gadgetsnow_name[0:50], gadgetsnow_image, gadgetsnow_link


def croma(name):
    try:
        global flipkart
        name1 = name.replace(" ", "+")
        flipkart = f'https://www.shopsy.in/search?q={name1}&sid=tyy%2C4io&as=on&as-show=on&pageUID=1678557787075'
        croma_link=flipkart
        res = requests.get(
            f'https://www.shopsy.in/search?q={name1}&sid=tyy%2C4io&as=on&as-show=on&pageUID=1678557787075',
            headers=headers)

        print("\nSearching in Shopsy....")
        soup = BeautifulSoup(res.text, 'html.parser')

        if (soup.select('.css-1dbjc4n.r-13awgt0.r-18u37iz.r-1w6e6rj.r-1f12yv3.r-kzbkwu.r-ttdzmv')):
            # flipkart_name = soup.select('._3Djpdu')[0].getText().strip().upper()
            # if name.upper() in flipkart_name:
            croma_price = soup.select('.css-901oao.r-cqee49.r-1vgyyaa.r-ubezar.r-1rsjblm')[0].getText().strip()
            croma_name = soup.select('._1PnKMA')[0].getText().strip()
            print("Shopsy:")
            print(croma_name)
            print(croma_price)
            print("---------------------------------")
            croma_images = soup.find_all('img')[0]
            croma_image = croma_images['src']

        return croma_price, croma_name[0:50], croma_image, croma_link
    except:
        print("Shopsy: No product found!")
        print("---------------------------------")
        croma_price = '0'
        croma_name = '0'
        croma_image = '0'
        croma_link = '0'
    return croma_price, croma_name[0:50], croma_image, croma_link
       



def convert(a):
    b = a.replace(" ", '')
    c = b.replace("INR", '')
    d = c.replace(",", '')
    d = d.replace("`", '')
    f = d.replace("₹", '')
    g = int(float(f))
    return g
