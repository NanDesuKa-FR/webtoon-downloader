import os
from requests_html import HTMLSession
import requests
import glob
session = HTMLSession()
cookies = dict(ageGatePass='true')
import subprocess
import time
from sys import platform

def Logo():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')
        
    print()
    print("                   ██     ██ ███████ ██████  ████████  ██████   ██████  ███    ██     ██████  ██")
    print("                   ██     ██ ██      ██   ██    ██    ██    ██ ██    ██ ████   ██     ██   ██ ██      ")
    print("                   ██  █  ██ █████   ██████     ██    ██    ██ ██    ██ ██ ██  ██     ██   ██ ██      ")
    print("                   ██ ███ ██ ██      ██   ██    ██    ██    ██ ██    ██ ██  ██ ██     ██   ██ ██      ")
    print("                    ███ ███  ███████ ██████     ██     ██████   ██████  ██   ████     ██████  ███████ ")
    print("                                                                                        By NanDesuKa?")

def menu():
    print("\n\n  Make a choice:\n  ------------------------------------\n  1) Download with link\n  2) Download the entire catalog\n  ------------------------------------")

def Downloader(link):
    r = session.get(link, cookies=cookies)

    allimg = r.html.xpath("/html/body/div[1]/div[2]/div[3]/div[1]/div/div/img")
    ogtitle = (r.html.xpath('//*[@id="toolbar"]/div[1]/div/a'))[0].attrs['title']
    name_ep = (r.html.xpath('//*[@id="toolbar"]/div[1]/div/h1'))[0].attrs['title']
    name = ogtitle
    counter = 1
    if not os.path.exists(name):
        os.makedirs(name)
    if not os.path.exists(name + "/" + name_ep):
        os.makedirs(name + "/" + name_ep)
        for element in allimg:
            if (element.attrs['data-url']).find("https://webtoon-phinf.pstatic.net/") != -1:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0', 'referer': 'http://www.webtoons.com'}
                imget = requests.get((element.attrs['data-url']).replace("?type=q90", ""), headers=headers)
                file = open(name + "/" + name_ep + "/" + str(counter).zfill(3) +".jpg", "wb")
                file.write(imget.content)
                file.close()
                counter += 1

def DownloadByLink():
    Logo()
    loop = True
    while loop == True:
        link = input("\n\n  Enter link: ")
        if link.find("https://www.webtoons.com/") != -1 and link.find("/viewer?title_no=") != -1 and link.find("&episode_no=") != -1:
            loop = False
            Downloader(link)
        else:
            Logo()
            DownloadByLink()

def BatchDownloader():
    Logo()
    loop = True
    counter = 0
    list_link_principal = []
    while loop == True:
        r = session.get("https://www.webtoons.com/fr/genre", cookies=cookies)
        alllink = r.html.xpath('//a/@href')
        for element in alllink:
           if element.find("https://www.webtoons.com/") != -1 and element.find("list?title_no=") != -1:
                Logo()
                list_link_principal.append(element)
                counter += 1
                print("\n\n  " + str(counter) + " webtoons available\n  ------------------------------------")

        loop = False
    all_link_check = []
    counter_global = 0
    for element2 in list_link_principal:
        r = session.get(element2, cookies=cookies)
        id = element2.split("title_no=")[1]
        eplast = (r.html.xpath('/html/body/div[1]/div[3]/div/div[2]/div[2]/div[1]/ul/li[1]/a')[0].attrs['href']).split('&episode_no=')[1]

        for x in range(1, int(eplast)):
            counter_global += 1
            all_link_check.append("https://www.webtoons.com/fr/nandesuka/nandesuka/nandesuka/viewer?title_no=" + id + "&episode_no=" + str(x))
            Logo()
            print("\n\n  " + str(counter) + " webtoons available\n  ------------------------------------\n  " + str(counter_global) + " episodes\n  ------------------------------------")

    counter_downloaded = 0
    for element3 in all_link_check:
        Logo()
        try:
            print("\n\n  " + str(counter) + " webtoons available\n  ------------------------------------\n  " + str(counter_global) + " episodes\n  ------------------------------------\n  " + str(counter_downloaded) + " / " + str(len(all_link_check)) + " episodes downloaded\n  ------------------------------------")
            Downloader(element3)
        except:
            console = False
        counter_downloaded += 1

if __name__ == "__main__":
    Logo()
    menu()
    loop = True
    while loop == True:
        reponse = input("  Choose 1 or 2: ")
        if reponse in ['1', '2']:
            Logo()
            loop = False
            if reponse == "1":
                DownloadByLink()
            elif reponse == "2":
                BatchDownloader()
        else:
            Logo()
            menu()