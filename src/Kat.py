import requests
from bs4 import BeautifulSoup
import time
import os
import sys

PRECIO01 = 350
PRECIO02 = 550 
VIP0 = 950
N = 0



def precios():
	os.system("clear")
	print("""
  __  __                 _                       _    _  _____ _____  
 |  \/  |               | |                     | |  | |/ ____|  __ \ 
 | \  / | ___  _ __  ___| |_ ___ _ __   ______  | |  | | (___ | |  | |
 | |\/| |/ _ \| '_ \/ __| __/ _ \ '__| |______| | |  | |\___ \| |  | |
 | |  | | (_) | | | \__ \ |_  __/ |             | |__| |____) | |__| |
 |_|  |_|\___/|_| |_|___/\__\___|_|              \____/|_____/|_____/ 
                                                                      
                                                                      

""")
	print("actualizacion: ", N)
	url = "https://transferwise.com/es/currency-converter/mxn-to-usd-rate#rate-alerts"
	s = requests.Session()

	response = s.get(url)
	#print(response.text)

	soup = BeautifulSoup(response.text, 'html.parser')
	pro = soup.find("span", {"class", "text-success"}).getText()
	cambio = soup.find("small", {"class", "m-r-1"}).getText()
	print("actualmente 1 MXN a USD esta en : ", pro)
	pro = pro.replace(',', '.')
	pro = float(pro)
	precio1 = pro*PRECIO01
	precio2 = pro*PRECIO02
	vip = pro*VIP0
	print("150 creditos -> ", precio1, "USD")
	print("300 creditos -> ",precio2, "USD")
	print("VIP -> ", vip, "USD")
	print("")
	print(cambio)
	print("")
	time.sleep(5)
	



while True:
	precios()
	N = N+1
