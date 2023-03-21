from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import pandas as pd

# simple way to find, the best way should use class child [n] to find the content
# However, in this case, the build name must have the details of Floor and Block

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

public_property_url = "https://hk.centanet.com/findproperty/list/buy?q=pOUaBGr6EqOAIcc5Nhzew"
private_property_url = 'https://hk.centanet.com/findproperty/list/buy?q=yw2IFqnk4EmYbCU7hDZMA'

driver.get(public_property_url)

r = driver.page_source
raw_data = BeautifulSoup(r, 'html.parser')

all_number = raw_data.find_all('li', attrs={'class':'number'})
bs4_num = BeautifulSoup(str(all_number), 'html.parser')
last_page = int(bs4_num.text[1:-1].split(', ')[-1])

house_list = []
house_detail = []

for page in range(1, last_page+1):
    print(f'page:{page}')

    spans = raw_data.find_all('span', attrs={'class':'title-lg'})
    for span in spans:
        house_list.append(span)

    spans2 = raw_data.find_all('span', attrs={'class':'title-sm'})
    for span in spans2:
        house_detail.append(span)

    try:
        next_button = driver.find_element(By.CSS_SELECTOR, f"i[class=\"el-icon el-icon-arrow-right\"]")
        time.sleep(1)
        next_button.click()
    except:
        print('not success, try again')
        next_button = driver.find_element(By.CSS_SELECTOR, f"i[class=\"el-icon el-icon-arrow-right\"]")
        time.sleep(1)
        next_button.click()

house_list_result = [BeautifulSoup(str(x), 'html.parser').text for x in house_list]
house_detail_result = [BeautifulSoup(str(x), 'html.parser').text for x in house_detail]

df = pd.DataFrame()
df['house_name'] = house_list_result
df['house_detail'] = house_detail_result
df.to_csv('demo.csv')