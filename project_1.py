# from bs4 import BeautifulSoup
# import requests

# URL = 'https://www.cian.ru/kupit-kvartiru/'
# r = requests.get(URL, headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"})

# soup = BeautifulSoup(r.content, 'html.parser')
# list_of_apartments ={}
# # class Parser:
# def search():
#     try:
#         if r.status_code == 200:
#             for i in soup.find_all('a', {'class':'_93444fe79c--link--eoxce'}):
#                 for j in range(len(soup.find_all('article', class_='_93444fe79c--container--Povoi _93444fe79c--cont--OzgVc'))):
#                     list_of_apartments[j]=i.get('href')


#                 return list_of_apartments



#     except Exception as e:
#         return f"mistake: {e}"   
# print(r.status_code)
# print(search())
# # parser = Parser()

# # print(parser.search)


from bs4 import BeautifulSoup
import requests

def search():
    URL = 'https://www.cian.ru/kupit-kvartiru/'
    headers = { 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    
    try:
        r = requests.get(URL, headers=headers)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html.parser')
            list_of_apartments = {}
            # Find all apartment link elements
            apartment_links = soup.find_all('a', {'class': '_93444fe79c--link--eoxce'})
            counter = 0
            for link in apartment_links:
                href = link.get('href')
                # Add the href to the dictionary with a unique key
                list_of_apartments[f'apartment_{counter} '] = href
                counter+=1
            for i in range(len(list_of_apartments)-1):
                if list_of_apartments[i].value == list_of_apartments[i+1].value:
                    list_of_apartments[i+1].pop()

# apartment_links.index(link)
            return list_of_apartments
        else:
            return f"Error: Unable to fetch data, status code: {r.status_code}"

    except Exception as e:
        return f"Error: {e}"

# Calling the search function and printing the result
print(search())