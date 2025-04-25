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

    def href(self):
        self.list_of_apartments = {}
        try:

            if self.r.status_code == 200:

                apartment_links = self.soup.find_all('a', {'class': '_93444fe79c--link--eoxce'})

                # counter = 0

                for link in apartment_links:
                    href = link.get('href')

                    self.list_of_apartments[f'apartment_{apartment_links.index(link)} '] = href
                keys = list(self.list_of_apartments.keys())
                for i in range(len(keys)):
                    self.list_of_apartments[i] = self.list_of_apartments.pop(keys[i])
                # apartment_links.index(link)

                return self.list_of_apartments


            else:

                return f"Error: Unable to fetch data, status code: {self.r.status_code}"





        except Exception as e:

            return f"Error: {e}"

    def name(self):
        self.list_of_name = {}
        try:


            if self.r.status_code == 200:




                apartment_links = self.soup.find_all('span', {'class': '_93444fe79c--color_text-main-default--HgSpe _93444fe79c--lineHeight_28px--KFXmc _93444fe79c--fontWeight_bold--BbhnX _93444fe79c--fontSize_22px--sFuaL _93444fe79c--display_block--KYb25 _93444fe79c--text--b2YS3 _93444fe79c--text_letterSpacing__normal--yhcXb'})

                for link in apartment_links:
                    name = link.text
                    self.list_of_name[f'Квартира №{apartment_links.index(link)}'] = name
                    # Add the href to the dictionary with a unique key

                #     list_of_apartments[f'apartment_{apartment_links.index(link)} '] = href
                # keys = list(list_of_apartments.keys())
                # for i in range(len(keys)):
                #     list_of_apartments[i] = list_of_apartments.pop(keys[i])
                # # apartment_links.index(link)
                #
                return self.list_of_name


            else:

                return f"Error: Unable to fetch data, status code: {self.r.status_code}"

        except Exception as e:

            return f"Error: {e}"
parser = Parser()
