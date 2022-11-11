import requests
from bs4 import BeautifulSoup
import os


class Games(object):
    page_games = None
    headers = {
            'Host': 'www.futeboleiro.com',
            'Sec-Ch-Ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'close',
        }
    
    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        
    def get_source_calendar_world_cup(self):
        """request page source in futeboleiro for get datetime for games world cup futball
        """
        response = self.session.get('https://www.futeboleiro.com/copa-do-mundo-2022/calendario/')
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            self.page_games = soup

    def find_games_in_page_table(self):
        game_time = self.page_games.find_all("div", {"class": "games-overview-table__date date-time"})
        game_teams = self.page_games.find_all("div", {"class": "games-overview-table__teams"})
        stadium = self.page_games.find_all("div", {"class": "games-overview-table__stadium stadium-name"})
        
        for x in range(0, len(game_teams)):
            print(f'o jogo entre {game_teams[x].text} ocorrerá no dia {game_time[x].text} no estádio {stadium[x].text}')


