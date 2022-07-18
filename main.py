import bs4
import requests
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

def title_search(articles):
    for article in articles:
        preview = article.find_all(class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
        preview = [prev.find("p").text for prev in preview]
        for prev in preview:
            for k in KEYWORDS:
                if k in prev:
                    title = article.find("h2").find("span").text
                    href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
                    data_time = article.find("time").attrs["title"]
                    print(f'\nДата: {data_time}\nЗаголовок: {title}\nсылка: {base_url+href}\n')

def article_search(articles):
    Flag = True
    for article in articles:
        preview = article.find_all(
            class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
        preview = [prev.find("p").text for prev in preview]
        for prev in preview:
            href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
            response1 = requests.get(base_url + href, headers=header)
            text_ = response1.text
            soup_ = bs4.BeautifulSoup(text_, features="html.parser")
            p_text = soup_.find_all("p")
            Flag = True
            while Flag:
                for p_text_ in p_text:
                    if Flag == False:
                        break
                    for keyword in KEYWORDS:
                        if keyword in p_text_.text:
                            title = article.find("h2").find("span").text
                            href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
                            data_time = article.find("time").attrs["title"]
                            print(f'\nДата: {data_time}\nЗаголовок: {title}\nсылка: {base_url + href}\n')
                            Flag = False
                            break
                if prev == '':
                    Flag = False

if __name__ == '__main__':
    header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/103.0.0.0 Safari/537.36'}
    base_url = "https://habr.com"
    url = base_url+"/ru/all/"
    response = requests.get(url, headers=header)
    text = response.text
    soup = bs4.BeautifulSoup(text, features="html.parser")
    articles = soup.find_all("article")
    print('Поиск по заголовку:')
    title_search(articles)
    print('Поиск по статье:')
    # article_search(articles)


