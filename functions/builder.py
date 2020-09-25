from bs4 import BeautifulSoup
import requests


def getObozNews(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, features="html.parser")
    news = soup.find_all("url")
    return news


def getListOfImg(url):
    imgList =[]
    fullNews = getObozNews(url)
    for news in fullNews:
        img = news.find("img", "newsImgRowTime_img lazyImg --desktopH160 --tabletH120")
        if img is not None:
            imgList.append(img.get("src"))
    return imgList


def getNewsList(url):
    newsList =[]
    structure = {}
    fullNews = getObozNews(url)
    for news in fullNews:
        title = news.find("news:title")
        img = news.find("image:loc")
        desc = news.find("news:keywords")
        if img is not None:
            structure["image"] = img.contents[0]
        if title is not None:
            structure["title"] = title.contents[0]
        if desc is not None:
            structure["desc"] = desc.contents[0]
        newsList.append(structure.copy())
        structure.clear()
    return newsList