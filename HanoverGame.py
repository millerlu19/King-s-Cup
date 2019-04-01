# HanoverGame.py

from bs4 import BeautifulSoup
import requests
import re

class HanoverGame:

    def __init__(self, page_url):
        req = requests.get(page_url)
        self.page = BeautifulSoup(req.content, 'html.parser')
        self.location = self.set_location()
        self.opponent = self.set_opponent()
        self.hanover_score = self.set_hanover_score()
        self.opponent_score = self.set_opponent_score()
        self.date = self.set_date()

    def __str__(self):
        return self.location + " | " + "Hanover: " + self.hanover_score + " | " + self.opponent + ": " \
               + self.opponent_score + " | " + self.date

    def set_location(self):
        game_info = self.page.find(class_='game-info')
        game_info_2 = list(game_info.children)[1].prettify()
        location_split = re.split('Location:\n    </th>\n    <td class="text">\n     ', game_info_2)
        location = re.split("\n", location_split[1])
        return location[0]

    def set_opponent(self):
        opponent_name = list(self.page.find(class_='head').children)[1].prettify()
        opponent_name = opponent_name.split()
        if opponent_name[1] == "Hanover":
            if len(opponent_name[3]) < 4 or opponent_name[3] == "Kent":
                if opponent_name[5] == "-":
                    opponent_name_list = opponent_name[3:7]
                    opponent_name_string = " ".join(opponent_name_list)
                    return opponent_name_string
                else:
                    opponent_name_list = opponent_name[3:6]
                    opponent_name_string = " ".join(opponent_name_list)
                    return opponent_name_string
            elif len(opponent_name[3]) == 4:
                opponent_name_list = opponent_name[3:5]
                opponent_name_string = " ".join(opponent_name_list)
                return opponent_name_string
            else:
                opponent_name_string = opponent_name[3]
                return opponent_name_string
        else:
            if len(opponent_name[1]) < 4 or opponent_name[1] == "Kent":
                if opponent_name[3] == "-":
                    opponent_name_list = opponent_name[1:5]
                    opponent_name_string = " ".join(opponent_name_list)
                    return opponent_name_string
                else:
                    opponent_name_list = opponent_name[1:4]
                    opponent_name_string = " ".join(opponent_name_list)
                    return opponent_name_string
            elif len(opponent_name[3]) == 4:
                opponent_name_list = opponent_name[1:3]
                opponent_name_string = " ".join(opponent_name_list)
                return opponent_name_string
            else:
                opponent_name_string = opponent_name[1]
                return opponent_name_string

    def set_hanover_score(self):
        if self.is_home_game():
            return self.set_home_score()
        else:
            return self.set_away_score()

    def set_opponent_score(self):
        if self.is_home_game():
            return self.set_away_score()
        else:
            return self.set_home_score()

    def is_home_game(self):
        if self.location == "Collier Arena -- Hanover, Ind." or self.location == "Collier Arena (Hanover, IN)":
            return True
        else:
            return False

    def set_home_score(self):
        home_score = self.page.find(class_='team-score home')
        home_total = list(home_score.children)[0]
        return home_total

    def set_away_score(self):
        away_score = self.page.find(class_='team-score visitor')
        away_total = list(away_score.children)[0]
        return away_total

    def set_date(self):
        date = list(self.page.find(class_='head').children)[1].prettify()
        date_split = re.split("<span>\n  ", date)
        game_date = re.split("\n", date_split[-1])
        return game_date[0]

    def get_location(self):
        return self.location

    def get_opponent(self):
        return self.opponent

    def get_hanover_score(self):
        return self.hanover_score

    def get_opponent_score(self):
        return self.opponent_score

    def get_date(self):
        return self.date