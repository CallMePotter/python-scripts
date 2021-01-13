import requests
from bs4 import BeautifulSoup

source = requests.get("https://check.torproject.org")
soup = BeautifulSoup(source.text, "html.parser")

ip = soup.find("div", {"class": "content"})
for line in ip.text.splitlines()[4:10]:
    if line != "":
        print(line.strip())
