from bs4 import BeautifulSoup
import json
import requests
import pandas as pd
def adv():
    # url = "http://www.nfl.com/standings"
    # url = "https://fastestlaps.com/tracks/adm-miachkovo"
    url = "https://www.nfl.com/standings/"
    # url= "https://www.nfl.com/standings/division/1999/REG"
    # url = " https://fastestlaps.com/tracks/adm-miachkovo"
    # url = "https://en.wikipedia.org/wiki/Ali_Gatie"
    # url = "https://github.com/fivethirtyeight/negro-leagues-player-ratings"
    # url = " https://en.wikipedia.org/wiki/List_of_European_Cup_and_UEFA_Champions_League_finals"
    # url = "https://en.wikipedia.org/wiki/List_of_NBA_champions"
    # url = " https://en.wikipedia.org/wiki/List_of_24_Hours_of_Le_Mans_winners"
    page = requests.get(url)
    # print(page.text)
    soup = BeautifulSoup(page.text, 'lxml')
    top={}
    # print(soup)
    title = soup.find('title')
    top['title']=title.text
    # print(title)
    # for title in title:
    #     heading=title.find_all('h1')
    #     for header in title:
    #         print(header.text, end='')
    #     print()
    tables = soup.find_all('table')
    top["tables"]=[]
    # print(tables)
    for table in tables:
        heading=table.find_all('th')
        # for header in heading:
        #     print(header.text, end='')
        # print()
        table_data=[]
        # for row in table.find_all('tr'):
        #     table_data.append([])
        for row in table.find_all('tr'):
            table_data.append([])
        j=0
        for row in table.find_all('tr'):
            for col in row.find_all('td'):
                # print(col.text, end='|')
                table_data[j].append(col.text)
            j+=1
        top["tables"].append(table_data)

    print(top)
    with open('topic.json',"w") as f:
        json.dump(top,f,indent=4)
    return top
data=adv()