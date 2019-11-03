from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import warnings
warnings.filterwarnings('ignore')

class Player():
    def __init__(self):
        self.name = ""
        self.link = ""

player_list = []

def get_player_list():
    driver = webdriver.PhantomJS(executable_path=r'C:\Users\Aalie\Downloads\phantomjs-2.1.1-windows\bin\phantomjs.exe')

    url = "https://stats.nba.com/players/list/"

    driver.get(url)

    source = driver.page_source

    soup = BeautifulSoup(source, 'lxml')
    # csv file to save data into a file
    csv_file = open('nba_player_list_with_link', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['name', 'link'])

    div = soup.find('div', class_="stats-player-list players-list")

    for a in div.find_all('a'):
        # print(a.text)
        # print(a['href'])
        player = Player()
        player.name = a.text
        link = a['href']
        player.link = f'https://stats.nba.com/{link}'
        player_list.append(player)

        csv_writer.writerow([player.name, player.link])

    for one_player in player_list:
        print(one_player.name)
        print(one_player.link)
        print()

    # remember to put this in the last
    csv_file.close()
    driver.quit()
    return player_list

get_player_list()