from dataclasses import replace
import requests
from bs4 import BeautifulSoup as btfs
from random import choices


class News:
    def __init__(self, search):
        self.search = search
        self.url_base_google = f'https://www.google.com/search?hl=fr&q={self.search}&tbm=nws&tbs=sbd:1'
        self.topics = [] # {'title': None, 'description': None, 'link': None}

    def searchTAG(self, html, tag, att):
        soup = btfs(html, features='html.parser')
        topics = soup.findAll(tag, att)
        return topics
    
    def formatHREF(self, href):
        return href.split('&')[0][7:]

    def formatDESC(self, desc):
        return '. '.join(desc.split('.')[0:-1])[0:120] + '...'
    
    def formatTITLE(self, title):
        return ' '.join(title.split(' ')[0:4])[0:25] + '...'

    def getTopics(self):
        req = requests.get(self.url_base_google).text
        topics = self.searchTAG(req, 'div', {'class': 'Gx5Zad fP1Qef xpd EtOod pkphOe'})
        return topics
    
    def fillTopicsNews(self):
        for tp in self.getTopics():
            href = tp.find('a')
            title = tp.find('div', {'class': 'BNeawe vvjwJb AP7Wnd'})
            descrition = tp.find('div', {'class': 'BNeawe s3v9rd AP7Wnd'})
            date = tp.find('span', {'class': 'r0bn4c rQMQod'})
            self.topics.append(
                {'title': self.formatTITLE(title.text), 
                'description': self.formatDESC(descrition.text), 
                'link': self.formatHREF(href.attrs['href']), 
                'date': date.text
                })
    
    @staticmethod
    def selectTopics(arrTopics, nTopics=4):
        return choices(arrTopics, k=nTopics)
        

if __name__ == '__main__':
    listTopics = []
    buscas = ['Atlassian jira', 'asana', 'gestion', 'outils+de+gestion']
    buscas = ['+'.join(i.split(' ')) for i in buscas]
    for busca in buscas:
        news = News(busca)
        print(news.url_base_google)
        news.fillTopicsNews()
        tp = News.selectTopics(news.topics, 1)[0]
        listTopics.append(tp)

        print(tp['title'])
        print(tp['description'])
        print(tp['link'])
        print(tp['date'])
        print('========================')
    
    print(requests.get(news.url_base_google).text)
