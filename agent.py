from selenium import webdriver
import os
import warnings

#use PATH accordingly
os.environ['PATH'] += r'C:\WebDriver\chromedriver.exe'

warnings.filterwarnings("ignore",category=DeprecationWarning)

driver = webdriver.Chrome()
driver.get('https://sothebysrealty.ca/en/find-an-agent/sort-az/province-on/')
driver.implicitly_wait(5)
try:
    ok = driver.find_element_by_xpath('//a[@class="btn btn-warning btn_gdpr"]')
    ok.click()
except:
    print('ok')


agent_name = driver.find_elements_by_xpath('//div[@class="content-split"]//div[@class="agent-name"]')

name = []
for i in agent_name:
    name.append(i.text.split())


contect = driver.find_elements_by_xpath('//div[@class="content-split"]//div[@class="agent-contact"]//a[@target="_blank"]')


contect_num = []
for i in contect:
    contect_num.append(i.get_attribute('href')[4:])


name_url = []
for i in name:
    name2 = '-'.join(i)
    name3 = name2.replace('(','').replace(')','').replace('.','').replace('é','e').replace("'",'')
    name_url.append(name3)


email = []
for i in name_url[:263]:
    url = f'https://sothebysrealty.ca/en/{i}/'
    driver.get(url)
    driver.implicitly_wait(10)
    ele = driver.find_element_by_xpath('//span[@class="contact_small"]//a[@class="orange"]')
    email.append(ele.text)


# i am appendind this to avoid error
email.append('')


import pandas as pd
dic = {'Name':name_url,'Contect_num':contect_num,'Email':email}
df =pd.DataFrame(dic)


df.to_csv('canada.csv')