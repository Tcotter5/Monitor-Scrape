#(in terminal) install BeautifulSoup // pip install beautifulsoup4// install requests // pip install requests
from bs4 import BeautifulSoup
import requests

#monitor url
url = "https://www.newegg.com/black-rgb-msi-optix-ag321cqr-32/p/N82E16824475132?Description=monitor&cm_re=monitor-_-24-475-132-_-Product&quicklink=true"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

# use $ sign to find numerical price
price = doc.find_all(text="$")

# 0 used to find first instance of $
parent = price[0].parent

# strong was the html branch needed to locate specific price
strong = parent.find("strong")
print(strong.string)