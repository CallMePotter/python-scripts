from bs4 import BeautifulSoup
import requests

link = "https://wanderinginn.com/table-of-contents"
source = requests.get(link).text
soup = BeautifulSoup(source, "html.parser")

for link in soup.find_all("a"):
    if link.text == "2.00":
        subsource = requests.get(link.get("href")).text
        subsoup = BeautifulSoup(subsource, "html.parser")

text = subsoup.find("div", {"class": "entry-content"})

formatted_text = ""

for paragraph in text.find_all("p"):
    formatted_text += str(paragraph.text) + "\n"

formatted_text.splitlines()[:-2]

for line in formatted_text.splitlines()[:-2]:
    print(line)
