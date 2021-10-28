import requests
from bs4 import BeautifulSoup
from datetime import datetime

date = datetime.today().strftime('%m-%d-%Y')
dateurl = date.replace('-','')

URL = "https://www.fantasylabs.com/mlb/lineups/?date=" + dateurl
page = requests.get(URL)
soup = BeautifulSoup(page.content,"html.parser")
##games = 