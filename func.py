
#Number 1
# from bs4 import BeautifulSoup
# import requests
# class Parser:
#     def __init__(self):

#         URL = 'https://www.cian.ru/kupit-kvartiru/'
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
#         }
#         self.r = requests.get(URL, headers=headers)
#         self.soup = BeautifulSoup(self.r.content, 'html.parser')

#     def href(self):
#         self.list_of_apartments = {}
#         try:

#             if self.r.status_code == 200:

#                 apartment_links = self.soup.find_all('a', {'class': '_93444fe79c--link--eoxce'})

#                 # counter = 0

#                 for link in apartment_links:
#                     href = link.get('href')

#                     self.list_of_apartments[f'apartment_{apartment_links.index(link)} '] = href
#                 keys = list(self.list_of_apartments.keys())
#                 for i in range(len(keys)):
#                     self.list_of_apartments[i] = self.list_of_apartments.pop(keys[i])
#                 # apartment_links.index(link)

#                 return self.list_of_apartments


#             else:

#                 return f"Error: Unable to fetch data, status code: {self.r.status_code}"





#         except Exception as e:

#             return f"Error: {e}"

#     def name(self):
#         self.list_of_name = {}
#         try:


#             if self.r.status_code == 200:




#                 apartment_links = self.soup.find_all('span', {'class': '_93444fe79c--color_text-main-default--HgSpe _93444fe79c--lineHeight_28px--KFXmc _93444fe79c--fontWeight_bold--BbhnX _93444fe79c--fontSize_22px--sFuaL _93444fe79c--display_block--KYb25 _93444fe79c--text--b2YS3 _93444fe79c--text_letterSpacing__normal--yhcXb'})

#                 for link in apartment_links:
#                     name = link.text
#                     self.list_of_name[f'Квартира №{apartment_links.index(link)}'] = name
#                     # Add the href to the dictionary with a unique key

#                 #     list_of_apartments[f'apartment_{apartment_links.index(link)} '] = href
#                 # keys = list(list_of_apartments.keys())
#                 # for i in range(len(keys)):
#                 #     list_of_apartments[i] = list_of_apartments.pop(keys[i])
#                 # # apartment_links.index(link)
#                 #
#                 return self.list_of_name


#             else:

#                 return f"Error: Unable to fetch data, status code: {self.r.status_code}"

#         except Exception as e:

#             return f"Error: {e}"
# parser = Parser()

#Number 2
from bs4 import BeautifulSoup
import requests
class Parser:
    def __init__(self):

        URL = 'https://www.cian.ru/kupit-kvartiru/'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        self.r = requests.get(URL, headers=headers)
        self.soup = BeautifulSoup(self.r.content, 'html.parser')
        self.list_of_apartments = []
        self.list_of_name = []
    def collection(self):

        try:
            if self.r.status_code == 200:
                # full_link = self.soup.find_all('div', {'class': '_93444fe79c--row--kEHOK_93444fe79c--row--kEHOK'})
                # print('testssss',full_link)
                # for linkall in full_link:
                apartaments = self.soup.findAll('a', {'class': '_93444fe79c--link--eoxce'})
                    # if linkall:
                    #     self.list_of_apartments.append(link.get('href'))
                    # else:
                    #     continue
                names = self.soup.findAll('span', {'class': '_93444fe79c--color_text-main-default--HgSpe _93444fe79c--lineHeight_28px--KFXmc _93444fe79c--fontWeight_bold--BbhnX _93444fe79c--fontSize_22px--sFuaL _93444fe79c--display_block--KYb25 _93444fe79c--text--b2YS3 _93444fe79c--text_letterSpacing__normal--yhcXb'})
                    # if linkall:
                    #     self.list_of_name.append(name.get_text())
                    # else:
                    #     continue
                # counter = 0
                #
                for link in apartaments:
                    href = link.get('href')
                    self.list_of_apartments.append(href)
                # self.list_of_apartments = set(self.list_of_apartments)
                for name in names:
                    name1 = name.text
                    self.list_of_name.append(name1)
                # self.list_of_name = set(self.list_of_name)
                # return [self.list_of_name, self.list_of_apartments]
            else:

                return f"Error: Unable to fetch data, status code: {self.r.status_code}"





        except Exception as e:

            return f"Error: {e}"

    # def name_1(self):
    #     return self.list_of_name
    # def hreF_1(self):
    #     return self.list_of_apartments


