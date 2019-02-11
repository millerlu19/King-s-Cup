# HCMBB_Stats.py

import requests
from bs4 import BeautifulSoup
#import HanoverGame.py

# def get_urls_dict()
# key = (opponent, date)
# value = url
def get_game_url_dict():
    """
    Returns a list of all the urls of each Hanover games' box scores.
    Two separate Dictionaries for the 2017-2018 season and the 2018-2019 season.
    """
    PageUrls = open('PageUrl.txt', 'r')

    Game_Urls_2018 = {}
    Game_Urls_2019 = {}

    for line in PageUrls:
        line = line.strip()
        if not line.startswith('#') and not len(line) == 0:
            opp, link = line.split(' = ')
            date = link.split('/')[-1].split('_')[0]
            opponent = (opp, date)
            date_int = int(date)
            if date_int <= 20180302:
                Game_Urls_2018[opponent] = link
            else:
                Game_Urls_2019[opponent] = link

    PageUrls.close()

    return Game_Urls_2018, Game_Urls_2019

# helper function that takes the url and opens the page through a get request and returns the page
def get_game_page(Game_Urls_2018, Game_Urls_2019):
    """Returns the specific game url for the game that is being selected."""

    szn_input = input("Which Hanover Men's Basketball season would you like to view? (2019 or 2018) ")
    if szn_input == 2019:
        opp_input =
    return

def create_game_objects():
    """Returns the info collected from the HanoverGame class for the selected game."""

    return

# main()
# Creates a long list of the box score urls for each game played
# Create a HanoverGame object for each game page url
    # dictionary -> key: tuple (opponent, month & day, year), value: HanoverGame object
def main():
    Game_Urls_2018 = get_game_url_dict()[0]
    print(Game_Urls_2018)
    Game_Urls_2019 = get_game_url_dict()[1]
    print(Game_Urls_2019)

    Game_Page = get_game_page(Game_Urls_2018, Game_Urls_2019)
    print(Game_Page)

main()