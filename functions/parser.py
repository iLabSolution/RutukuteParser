import requests


# parser by tag
def getSomething(obj, tag):
    start = str("<" + tag + ">")
    end = str("</" + tag + ">")
    foo = obj.split(start)
    try:
        boo = foo[1]
        doo = boo.split(end)
        return doo[0]
    except:
        return ""


def getXMLNews(url):
    # Open RSS and convert data to string
    data = requests.get(url)
    data.encoding = data.apparent_encoding
    html = data.text
    string = str(html)

    # Split full news and pop info about ->xml
    listOfElement = string.split("<url>")
    listOfElement.pop(0)
    newsList = []
    newsDict = {}

    # fill newsList
    for x in listOfElement:
        newsDict["link"] = getSomething(x, "loc")
        newsDict["title"] = getSomething(x, "news:title").replace("&quot;", '"')
        newsDict["image"] = getSomething(x, "image:loc").replace("&quot;", '"')
        newsDict["desc"] = getSomething(x, "news:keywords").replace("&quot;", '"')
        print(newsDict)
        newsList.append(newsDict.copy())
        newsDict.clear()
    return newsList
