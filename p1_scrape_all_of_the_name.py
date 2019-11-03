from selenium import webdriver
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore')
driver = webdriver.PhantomJS(executable_path=r'C:\Users\Aalie\Downloads\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url = "https://stats.nba.com/players/list/"

driver.get(url)

source = driver.page_source


soup = BeautifulSoup(source, 'lxml')

div = soup.find('div', class_="stats-player-list players-list")

for a in div.find_all('a'):
    print(a.text)

# print(div)

# remember to put this in the last
driver.quit()
