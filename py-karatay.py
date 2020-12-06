import lxml
from bs4 import BeautifulSoup as bs
import requests

url_karatay = "https://karatay.edu.tr/"

request_duyurular = requests.get(url_karatay + "Duyurular").text
soup_duyurular = bs(request_duyurular, "lxml")

duyurular = soup_duyurular.find("table", attrs={"id": "datatable1"}).\
    find("tbody").find_all("tr")

file = open("karatay_duyurular.txt", "w")

for i in range(0, len(duyurular)):
    print("="*50)
    url_find = duyurular[i].find("td").find("a")
    link = url_find["href"]
    print(link)

    detail_page = requests.get(url_karatay + link)
    duyuru_detail = bs(detail_page.content, "lxml")

    try:
        duyuru_detail_content = duyuru_detail.find("div",
                                                    attrs={"class": "content-wrap"}).text
    except:
        pass

    print(duyurular[i].text.strip())

    print("*"*25 + "Content" + "*"*25)

    print(duyuru_detail_content.strip())
    print("="*50)
    try:
        file.write("="*50 + "\n" + duyurular[i].text.strip() + "\n" + "*"*25 +
            "Content" + "*"*25 + "\n" + duyuru_detail_content.strip() + "\n" + "="*50)
    except:
        pass
file.close()
print("bitti")